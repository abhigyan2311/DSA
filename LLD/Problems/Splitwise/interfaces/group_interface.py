from abc import ABC, abstractmethod
from typing import List


class IGroupService(ABC):
    @abstractmethod
    def addGroup(self, groupId: str, name: str, members: List[str]):
        pass
