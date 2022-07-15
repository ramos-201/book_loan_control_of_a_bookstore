from typing import List


class ConsoleOutput:

    def __init__(self, text: str):
        self._text = text

    def write(self, text: str = None) -> None:
        if text:
            self._text = text

        if self._text is not None:
            print(self._text)

    def write_error(self) -> None:
        self.write(text=f'ERROR!: {self._text}')

    def write_dict_list(self, data: List[dict]) -> None:
        self.write()
        for item in data:
            for key, value in item.items():
                self.write(text=f'{key} : {value}')
