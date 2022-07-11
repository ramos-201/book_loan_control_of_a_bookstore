from views.options.option import Option
from views.utils.console_output import ConsoleOutput


class ShowBookOption(Option):

    def __init__(self,  option: str = None, description: str = None, data: list = None):
        super().__init__(description=description)
        self._option = option
        self._data_book = data

    def run(self) -> None:
        if self._data_book:
            for book in self._data_book:
                for key, value in book.items():
                    ConsoleOutput(text=f"{key} : {value}").write()
        else:
            print(self._description, " : ", self._option)
