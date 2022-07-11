class ConsoleOutput:

    def __init__(self, text: str = None):
        self._text = text

    def write(self) -> None:
        print(self._text)

    def write_error(self):
        print(f"ERROR!: {self._text}")
