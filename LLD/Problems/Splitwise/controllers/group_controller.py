class GroupController:
    def __init__(self, groupService) -> None:
        self._groupService = groupService

    def addGroup(self, groupId, name, members):
        return self._groupService.addGroup(groupId, name, members)
