import uuid
from typing import List

from app.model.book import Book
from app.repository.book_repository import BookRepository


def create_book(title: str, description: str, amount: int) -> uuid:
    book = Book(title=title, description=description, amount=amount)
    repository = BookRepository()
    repository.insert(book=book)

    return book.id


def get_books(**kwargs) -> List[dict]:
    repository = BookRepository()

    if kwargs:
        data_filter = {}
        for key, value in kwargs.items():
            data_filter[key] = value

        books = repository.filter(data=data_filter)
        response_books = _get_list_books(books=books)

    else:
        books = repository.get_books()
        response_books = _get_list_books(books=books)

    return response_books


def _get_list_books(books):
    response_books = []
    for book in books:
        response_books.append(book.to_dict())

    return response_books
