from typing import List

from app.model.book import Book
from app.repository.book_repository import BookRepository


class BookController:

    _book_repository = BookRepository()

    def create_book(self, title: str, description: str, amount: int) -> str:
        book = Book(title=title, description=description, amount=amount)
        self._book_repository.insert(book=book)

        return book.id

    def get_books(self, **kwargs) -> List[dict]:
        if kwargs:
            data_filter = {}

            for key, value in kwargs.items():
                data_filter[key] = value

            books = self._book_repository.filter(data=data_filter)
            response_books = self._get_list_books(books=books)
        else:
            books = self._book_repository.get_books()
            response_books = self._get_list_books(books=books)

        return response_books

    def _get_list_books(self, books: List[Book]) -> List[dict]:
        response_books = []

        for book in books:
            response_books.append(book.to_dict())

        return response_books
