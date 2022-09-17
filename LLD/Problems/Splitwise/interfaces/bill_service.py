from abc import ABC, abstractmethod
from typing import Dict


class IBillService(ABC):
    @abstractmethod
    def addBill(self, billId: str, title: str, groupId: str, amount: float, paidBy: Dict, contributions: Dict):
        pass
