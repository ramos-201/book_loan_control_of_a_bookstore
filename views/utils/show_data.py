from typing import List

from app.controller.book_controller import BookController
from views.utils.console_output import ConsoleOutput


class ShowData:

    def __init__(self, text: str, data_filter: dict = None):
        self._text = text
        self._data_filter = data_filter

    def show_data(self, data: List[dict]) -> None:
        ConsoleOutput(text=self._text).write_dict_list(data=data)

    def show_book_with_filter(self) -> None:
        book_controller = BookController()
        books = book_controller.get_books(data_filter=self._data_filter)
        self.show_data(data=books)
