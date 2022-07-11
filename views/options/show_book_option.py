from typing import List

from app.controller.book_controller import get_books
from views.options.option import Option
from views.utils.console_output import ConsoleOutput


class ShowBookOption(Option):

    def __init__(self,   description: str = "Show Book", option: str = None, data: List[dict] = None):
        super().__init__(description=description)
        self._option = option
        self._data_book = data

    def run(self) -> None:
        if self._data_book:
            self._show_book(books=self._data_book)
        else:
            if self._option == "show_all_book":
                books = get_books()
                self._show_book(books=books)

    def _show_book(self, books: List[dict]) -> None:
        ConsoleOutput(text=self._description)
        for book in books:
            for key, value in book.items():
                ConsoleOutput(text=f"{key} : {value}").write()
