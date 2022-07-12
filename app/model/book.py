import uuid


class Book:

    def __init__(self, title: str, description: str, amount: int):
        self._id = str(uuid.uuid4())
        self._title = title
        self._description = description
        self._amount = amount

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def amount(self):
        return self._amount

    def to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "description": self._description,
            "amount": self._amount
        }
