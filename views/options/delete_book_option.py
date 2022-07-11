from views.options.option import Option


class DeleteBookOption(Option):

    def __init__(self):
        super().__init__(description="Delete Book")

    def run(self) -> None:
        print(self._description)
