class User:
    def __init__(self) -> None:
        self._userId = None
        self._name = None

    @property
    def userId(self) -> str:
        return self._userId

    @userId.setter
    def userId(self, userId: str) -> None:
        self._userId = userId

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name
