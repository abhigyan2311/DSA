from typing import List


class Group:
    def __init__(self) -> None:
        self._groupId = None
        self._name = None
        self._members = None

    @property
    def groupId(self) -> str:
        return self._groupId

    @groupId.setter
    def groupId(self, groupId: str) -> None:
        self._groupId = groupId

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name
