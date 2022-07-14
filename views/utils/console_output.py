from typing import List


class ConsoleOutput:

    def __init__(self, text: str):
        self._text = text

    def write(self) -> None:
        print(self._text)

    def write_error(self) -> None:
        print(f'ERROR!: {self._text}')

    def write_list_dict(self, data: List[dict]) -> None:
        self.write()
        for d in data:
            for k, v in d.items():
                print(f'{k} : {v}')
