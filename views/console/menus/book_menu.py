from typing import List

from views.console.options.create_book_option import CreateBookOption
from views.console.options.delete_book_option import DeleteBookOption
from views.console.options.show_book_option import ShowBookOption
from views.console.options.update_book_option import UpdateBookOption
from views.console.menus.menu import Menu
from views.console.options.option import Option


class BookMenu(Menu):

    _description = '..:: Book Menu ::..'

    def _get_menu_options(self) -> List[Option]:
        self._exit_menu_option(description="Previous Menu")
        options = [
            CreateBookOption(),
            UpdateBookOption(description="Update Book", option="update_book"),
            UpdateBookOption(description="Add Book", option="add_book"),
            ShowBookOption(description="Show All Book", option="show_all_book"),
            ShowBookOption(description="Show Book", option="show_book"),
            ShowBookOption(description="Show Borrowed Books", option="show_borrowed_books"),
            ShowBookOption(description="Show Book Storage", option="show_book_storage"),
            ShowBookOption(description="Show Books Pending Delivery", option="show_books_pending_delivery"),
            ShowBookOption(description="The Book Is Available", option="show_if_the_book_is_available"),
            ShowBookOption(description="Show Book Available", option="show_book_available"),
            DeleteBookOption(),
            self._exit_option,
        ]

        return options
