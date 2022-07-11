from abc import abstractmethod
from typing import List

from views.options.exit_option import ExitOption
from views.options.option import Option
from views.utils.console import Console


class Menu:

    _description = None
    _exit_option = None

    def __init__(self):
        self._menu_options = self._get_menu_options()

    @abstractmethod
    def _get_menu_options(self) -> List[Option]:
        pass

    def run(self) -> None:
        while not self._exit_option.is_exit():
            self._show_menu_options()
            menu_option = self._get_menu_option()
            self._menu_options[menu_option - 1].run()

    def _show_menu_options(self) -> None:
        for i, value in enumerate(self._menu_options):
            print(f'{i + 1} :  {value.description}')

    def _get_menu_option(self) -> int:
        while True:
            response_option = Console(text='Write a menu option (int): ').read_int_is_positive()
            if response_option <= len(self._menu_options):
                break
            else:
                print("ERROR!, Enter a valid value")

        return response_option

    def _exit_menu_option(self, description: str):
        self._exit_option = ExitOption(description=description)
