from abc import ABC, abstractmethod

class ISpecialEntity(ABC):
    @abstractmethod
    def __init__(self, start: int, end: int) -> None:
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def se_id(self):
        pass
