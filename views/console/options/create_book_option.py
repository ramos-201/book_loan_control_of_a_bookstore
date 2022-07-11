from app.controller.book_controller import create_book, filter_book
from views.console.options.option import Option
from views.console.options.show_book_option import ShowBookOption


class CreateBookOption(Option):

    def __init__(self):
        super().__init__(description="Create Book")

    def run(self) -> None:
        title = input("Title of the book: ")
        description = input("Description of the book: ")
        amount = int(input("Number of books to enter: "))  # validate int

        created_book = create_book(title=title, description=description, amount=amount)

        data_book = filter_book(id_book=created_book)
        show_book_option = ShowBookOption(option="show_book", data=data_book)
        show_book_option.run()
