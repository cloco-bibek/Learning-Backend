from fastapi import Body, FastAPI


app = FastAPI()

BOOKS = [
    {'title': 'title one', 'author': 'author one', 'category': 'science'},
    {'title': 'title two', 'author': 'author two', 'category': 'math'},
    {'title': 'title three', 'author': 'author three', 'category': 'social'},
    {'title': 'title four', 'author': 'author four', 'category': 'math'},
    {'title': 'title five', 'author': 'author five', 'category': 'health'},
    {'title': 'title six', 'author': 'author two', 'category': 'math'},
]


@app.get("/books")
async def read_all_books():
    return BOOKS



# @app.get("/books/myBooks")
# async def read_all_books():
#     return {'mybooks': 'this is my books'}

# the above mybooks url is created before dynamic_params
# because python code runs chronologically so if dynamic_param
# statement runs before myBooks the myBooks params wont run as python
# will think mybooks is also a dynamic_param




# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param: str):
#     return {'dynamic_param': dynamic_param}



# below is example of etting data by passing path parameter
@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
# %20 means space
# casefold means to lowercase



# below is example of query parameters
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return



# below is example of using both path and  query parameters
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            book_to_return.append(book)

    return book_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)




@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book



@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
