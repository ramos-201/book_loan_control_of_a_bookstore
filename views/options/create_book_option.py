from app.controller.book_controller import create_book, filter_book
from views.options.option import Option
from views.options.show_book_option import ShowBookOption
from views.utils.console import Console


class CreateBookOption(Option):

    def __init__(self):
        super().__init__(description="Create Book")

    def run(self) -> None:
        title = Console(text="Title of the book: ").read_str_is_required()
        description = Console(text="Description of the book: ").read_str_is_required()
        amount = Console(text="Number of books to enter: ").read_int_is_positive()

        created_book = create_book(title=title, description=description, amount=amount)

        data_book = filter_book(id_book=created_book)
        show_book_option = ShowBookOption(option="show_book", data=data_book)
        show_book_option.run()
