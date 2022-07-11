from abc import abstractmethod


class Option:

    def __init__(self, description: str):
        self._description = description

    @property
    def description(self) -> str:
        return self._description

    @abstractmethod
    def run(self) -> None:
        pass
