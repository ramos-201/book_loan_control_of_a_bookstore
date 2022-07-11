from views.options.option import Option


class UpdateBookOption(Option):

    def __init__(self, description: str, option: str):
        super().__init__(description=description)
        self._option = option

    def run(self) -> None:
        print(self._description, " : ", self._option)
