from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

BOOKS = [
    Book(1, 'Computer Science Pro', 'Jack', 'A very nice book!', 5),
    Book(2, 'javascript', 'Russel', 'be javascript developer', 3),
    Book(3, 'python', 'Andy', 'be python developer', 4),
    Book(4, 'ruby', 'Harry', 'be ruby developer', 2),
    Book(5, 'php', 'Mia', 'be php developer', 3),
    Book(6, 'golang', 'karen', 'be golang developer', 4),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
