from app.controller.book_controller import BookController
from views.menus.book_filter_menu import BookFilterMenu
from views.options.option import Option
from views.utils.show_book_output import ShowBookOutput


class ShowBookOption(Option):

    def __init__(self,   description: str = 'Show Book', option: str = None):
        super().__init__(description=description)
        self._option = option

    def run(self) -> None:
        book_controller = BookController()
        if self._option == 'show_all_book':
            books = book_controller.get_books()
            ShowBookOutput(text=self._description).show_data(data=books)
        elif self._option == "show_book":
            BookFilterMenu().run()
