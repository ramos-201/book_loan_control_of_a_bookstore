from views.console.options.option import Option


class ExitOption(Option):

    def __init__(self, description: str):
        super().__init__(description=description)
        self._is_exit = False

    def is_exit(self) -> bool:
        return self._is_exit

    def run(self) -> None:
        self._is_exit = True
