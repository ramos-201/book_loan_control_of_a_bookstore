class Console:

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
                print("ERROR! This field is required, please enter a text")

        return response

    def read_int(self) -> int:
        while True:
            try:
                response = int(self.read_str())
                break
            except ValueError:
                print("ERROR! Enter a (int) formatted value.")

        return response

    def read_int_is_positive(self) -> int:
        while True:
            response = self.read_int()

            if response > 0:
                break
            else:
                print("ERROR! Please enter a number greater than 0")

        return response
