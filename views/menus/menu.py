from abc import abstractmethod
from typing import List

from views.options.exit_option import ExitOption
from views.options.option import Option
from views.utils.console_input import ConsoleInput
from views.utils.console_output import ConsoleOutput


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
        ConsoleOutput(text=f'{self._description}').write()

        for i, value in enumerate(self._menu_options):
            ConsoleOutput(text=f'{i + 1} :  {value.description}').write()

    def _get_menu_option(self) -> int:
        while True:
            response_option = ConsoleInput(text='Write a menu option (int): ').read_int_is_positive()

            if response_option <= len(self._menu_options):
                break
            else:
                ConsoleOutput(text='Enter a valid value').write_error()

        return response_option

    def _exit_menu_option(self, description: str) -> None:
        self._exit_option = ExitOption(description=description)
