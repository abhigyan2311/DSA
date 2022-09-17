from typing import List
from interfaces.user_service import IUserService
from models.user import User


class UserService(IUserService):
    def __init__(self) -> None:
        super().__init__()
        self.allUsers = dict()

    def addUser(self, userId: str, name: str):
        newUser = User()
        newUser.userId = userId
        newUser.name = name

        self.allUsers[userId] = newUser

        return newUser
