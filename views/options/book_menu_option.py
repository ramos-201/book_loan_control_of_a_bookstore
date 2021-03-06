from views.menus.book_menu import BookMenu
from views.options.option import Option


class BookMenuOption(Option):

    def __init__(self):
        super().__init__(description='Book Menu')

    def run(self) -> None:
        BookMenu().run()
