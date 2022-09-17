from typing import List
from interfaces.group_interface import IGroupService
from models.group import Group


class GroupService(IGroupService):
    def __init__(self) -> None:
        super().__init__()
        self.allGroups = dict()

    def addGroup(self, groupId: str, name: str, members: List[str]):
        newGroup = Group()
        newGroup.groupId = groupId
        newGroup.name = name
        newGroup.members = members

        self.allGroups[groupId] = newGroup

        return newGroup
