from typing import List

from views.options.book_menu_option import BookMenuOption
from views.menus.menu import Menu
from views.options.option import Option


class MainMenu(Menu):

    _description = '..:: Main Menu ::..'

    def _get_menu_options(self) -> List[Option]:
        self._exit_menu_option(description="Exit Menu")
        options = [
            BookMenuOption(),
            self._exit_option,
        ]

        return options
