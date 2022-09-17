from typing import Dict
from interfaces.bill_service import IBillService
from models.bill import Bill


class BillService(IBillService):
    def __init__(self) -> None:
        super().__init__()
        self.allBills = dict()

    def addBill(self, billId: str, title: str, groupId: str, amount: float, paidBy: Dict, contributions: Dict):
        newBill = Bill()
        newBill.billId = billId
        newBill.title = title
        newBill.groupId = groupId
        newBill.amount = amount
        newBill.paidBy = paidBy
        newBill.contributions = contributions

        self.allBills[billId] = newBill

        return newBill
