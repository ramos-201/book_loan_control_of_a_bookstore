import uuid
from typing import List

from app.model.book import Book
from app.repository.book_repository import BookRepository


def create_book(title: str, description: str, amount: int) -> uuid:
    book = Book(title=title, description=description, amount=amount)
    repository = BookRepository()
    repository.insert(book=book)

    return book.id


def filter_book(id: uuid) -> List[dict]:
    repository = BookRepository()
    books = repository.filter(id=id)
    response_books = []

    for book in books:
        response_books.append(book.to_dict())

    return response_books
