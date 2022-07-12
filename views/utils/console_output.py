class ConsoleOutput:

    def __init__(self, text: str):
        self._text = text

    def write(self) -> None:
        print(self._text)

    def write_error(self) -> None:
        print(f'ERROR!: {self._text}')
