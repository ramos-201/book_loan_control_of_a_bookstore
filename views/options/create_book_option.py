from app.controller.book_controller import BookController
from views.options.option import Option
from views.options.show_book_option import ShowBookOption
from views.utils.console_input import ConsoleInput
from views.utils.console_output import ConsoleOutput
from views.utils.show_book_output import ShowBookOutput


class CreateBookOption(Option):

    def __init__(self):
        super().__init__(description='Create Book')

    def run(self) -> None:
        ConsoleOutput(text=self._description).write()

        title = ConsoleInput(text='Title of the book: ').read_str_is_required()
        description = ConsoleInput(text='Description of the book: ').read_str_is_required()
        amount = ConsoleInput(text='Number of books to enter: ').read_int_is_positive()

        book_controller = BookController()
        created_book = book_controller.create_book(title=title, description=description, amount=amount)

        ShowBookOutput(text="Show Book").show_data_whit_filter(data_filter={"id": created_book})
