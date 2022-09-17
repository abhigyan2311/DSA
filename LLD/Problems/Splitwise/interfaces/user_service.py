from abc import ABC, abstractmethod


class IUserService(ABC):
    @abstractmethod
    def addUser(self, userId: str, name: str):
        pass
