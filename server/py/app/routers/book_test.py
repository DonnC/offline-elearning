from fastapi import APIRouter
from fastapi.responses import JSONResponse

import uuid

router = APIRouter(
    prefix="/book-test",
    tags=["book-test"],
    responses={404: {"description": "Not found"}},
)

books = [
    {
        "id": uuid.uuid4().hex,
        "title": "Champions run",
        "author": "DonnC Lab",
        "read": False,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Down the river",
        "author": "DonnC Lab",
        "read": False,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Mpho search",
        "author": "DonnC Lab",
        "read": False,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Kill Bill",
        "author": "DonnC Lab",
        "read": True,
    },
]

@router.get("/ping")
def ping():
    return JSONResponse({
        "status": "pong!"
    })

@router.get("/{book_id}")
def get_book(book_id):

    for book in books:
        if book['id'] == book_id:
            return JSONResponse(book)

    return JSONResponse(
        {
            "status": "error!",
            "books": f"book with id {book_id} not found"
        }
    )

@router.delete("/{book_id}")
def del_book(book_id):
    response_object = {'status': 'success'}

    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            response_object['message'] = f'Book: {book_id} removed!'
            return JSONResponse(response_object)

    response_object['message'] = f"book with id {book_id} not found"
    response_object['status'] = "error!"

    return JSONResponse(response_object)

@router.post("/")
def add_book(book: dict):
    response_object = {'status': 'success'}

    books.append({
             "id": uuid.uuid4().hex,
            'title': book.get('title'),
            'author': book.get('author'),
            'read': book.get('read')
        })

    response_object['message'] = 'Book added!'
  
    return JSONResponse(response_object)

@router.get("/")
def all_books():
    return JSONResponse(
        {
            "status": "success!",
            "books": books
        }
    )