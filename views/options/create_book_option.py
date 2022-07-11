from app.controller.book_controller import create_book, filter_book
from views.options.option import Option
from views.options.show_book_option import ShowBookOption
from views.utils.console_input import ConsoleInput


class CreateBookOption(Option):

    def __init__(self):
        super().__init__(description="Create Book")

    def run(self) -> None:
        title = ConsoleInput(text="Title of the book: ").read_str_is_required()
        description = ConsoleInput(text="Description of the book: ").read_str_is_required()
        amount = ConsoleInput(text="Number of books to enter: ").read_int_is_positive()

        created_book = create_book(title=title, description=description, amount=amount)

        books = filter_book(id=created_book)

        show_book_option = ShowBookOption(data=books)
        show_book_option.run()
