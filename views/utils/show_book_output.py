from typing import List

from app.controller.book_controller import BookController
from views.utils.console_output import ConsoleOutput


class ShowBookOutput:

    def __init__(self, text: str):
        self._text = text

    def show_data(self, data: List[dict]):
        ConsoleOutput(text=self._text).write_list_dict(data=data)

    def show_data_whit_filter(self, data_filter: dict):
        book_controller = BookController()
        books = book_controller.get_books(data_filter=data_filter)
        self.show_data(data=books)
