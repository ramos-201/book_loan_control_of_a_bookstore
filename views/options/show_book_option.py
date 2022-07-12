from typing import List

from app.controller.book_controller import get_books
from views.options.option import Option
from views.utils.console_output import ConsoleOutput


class ShowBookOption(Option):

    def __init__(self,   description: str = 'Show Book', option: str = None, data: List[dict] = None):
        super().__init__(description=description)
        self._option = option
        self._data_books = data

    def run(self) -> None:
        if self._data_books:
            self._show_books(books=self._data_books)
        else:
            if self._option == 'show_all_book':
                books = get_books()
                self._show_books(books=books)

    def _show_books(self, books: List[dict]) -> None:
        ConsoleOutput(text=self._description).write()

        for book in books:
            for key, value in book.items():
                ConsoleOutput(text=f'{key} : {value}').write()
