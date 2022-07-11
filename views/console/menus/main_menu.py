from typing import List

from views.console.options.book_menu_option import BookMenuOption
from views.console.menus.menu import Menu
from views.console.options.option import Option


class MainMenu(Menu):

    _description = 'Main Menu'

    def _get_menu_options(self) -> List[Option]:
        self._exit_menu_option(description="Exit Menu")
        options = [
            BookMenuOption(),
            self._exit_option,
        ]

        return options
