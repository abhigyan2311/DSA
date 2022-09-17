from typing import Dict
from models.user import User


class Bill:
    def __init__(self) -> None:
        self._billId = None
        self._title = None
        self._groupId = None
        self._amount = None
        self._paidBy = None
        self._contributions = None

    @property
    def billId(self) -> str:
        return self._billId

    @billId.setter
    def billId(self, billId: str) -> None:
        self._billId = billId

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @property
    def groupId(self) -> str:
        return self._groupId

    @groupId.setter
    def groupId(self, groupId: str) -> None:
        self._groupId = groupId

    @property
    def amount(self) -> str:
        return self._amount

    @amount.setter
    def amount(self, amount: str) -> None:
        self._amount = amount

    @property
    def paidBy(self) -> str:
        return self._paidBy

    @paidBy.setter
    def paidBy(self, paidBy: Dict) -> None:
        self._paidBy = paidBy

    @property
    def contributions(self) -> str:
        return self._contributions

    @contributions.setter
    def contributions(self, contributions: Dict) -> None:
        self._contributions = contributions
