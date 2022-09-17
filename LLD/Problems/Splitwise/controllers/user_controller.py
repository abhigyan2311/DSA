class UserController:
    def __init__(self, userService) -> None:
        self._userService = userService

    def addUser(self, userId, name):
        return self._userService.addUser(userId, name)
