from typing import List

from views.menus.menu import Menu
from views.options.Book_filter_option import BookFilterOption
from views.options.option import Option


class BookFilterMenu(Menu):

    _description = '..:: Book Filter Menu ::..'

    def _get_menu_options(self) -> List[Option]:
        self._exit_menu_option(description='Previous Menu')
        options = [
            BookFilterOption(description='Search by id', key_search='id'),
            BookFilterOption(description='Search by title', key_search='title'),
            self._exit_option,
        ]

        return options
