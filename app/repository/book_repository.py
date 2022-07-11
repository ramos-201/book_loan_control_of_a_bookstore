import uuid
from typing import List

from app.model.book import Book


class BookRepository:
    _books = []

    def insert(self, book: Book) -> None:
        self._books.append(book)

    def filter(self, id: uuid) -> List[Book]:
        books = []
        for book in self._books:
            if book.id == id:
                books.append(book)

        return books
