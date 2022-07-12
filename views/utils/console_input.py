from views.utils.console_output import ConsoleOutput


class ConsoleInput:

    def __init__(self, text: str):
        self._text = text

    def read_str(self) -> str:
        return input(self._text)

    def read_str_is_required(self) -> str:
        while True:
            response = self.read_str()

            if len(response) > 0:
                break
            else:
                ConsoleOutput(text='This field is required, please enter a text').write_error()

        return response

    def read_int(self) -> int:
        while True:
            try:
                response = int(self.read_str())
                break
            except ValueError:
                ConsoleOutput(text='Enter a (int) formatted value.').write_error()

        return response

    def read_int_is_positive(self) -> int:
        while True:
            response = self.read_int()

            if response > 0:
                break
            else:
                ConsoleOutput(text='Please enter a number greater than 0').write_error()

        return response
