from typing import List

from app.model.book import Book


class BookRepository:
    _books = []

    def insert(self, book: Book) -> None:
        self._books.append(book)

    def filter(self, data: dict) -> List[Book]:
        books = []
        for key, value in data.items():
            for book in self._books:
                if book.__getattribute__(key) == value:
                    books.append(book)

        return books

    def get_books(self) -> List[Book]:
        return self._books
