from views.options.option import Option
from views.utils.console_input import ConsoleInput
from views.utils.show_data import ShowData


class BookFilterOption(Option):

    def __init__(self, description: str = None, key_search: str = None):
        super().__init__(description=description)
        self._key_search = key_search

    def run(self) -> None:
        data_filter = self._get_str_filter()
        ShowData(text="Show Book", data_filter={self._key_search: data_filter}).show_book_with_filter()

    def _get_str_filter(self):
        return ConsoleInput(text=f'Enter the data ({self._key_search}) of the book: ').read_str()
