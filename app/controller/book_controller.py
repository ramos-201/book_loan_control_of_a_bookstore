from typing import List

from app.model.book import Book


def create_book(title: str, description: str, amount: int) -> str:
    print(f"created_book, {title}, {description}, {amount}")
    return "1234"


def filter_book(id_book: str) -> List[Book]:
    print(f"filter_book, {id_book}")
    return [Book().dict()]
