from app.model.book import Book
from app.repository.book_repository import BookRepository


def test_insert_success():
    book = Book(title="title", description="description", amount=12)
    repository = BookRepository()
    repository.insert(book=book)

    book_result = repository.filter(data={"id": book.id})
    assert isinstance(book, (type(book_result[0])))
    assert book.id == book_result[0].id

