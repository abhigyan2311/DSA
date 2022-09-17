from typing import Dict


class BillController:
    def __init__(self, billService) -> None:
        self._billService = billService

    def addBill(self, billId: str, title: str, groupId: str, amount: float, paidBy: Dict, contributions: Dict):
        return self._billService.addBill(billId, title, groupId, amount, paidBy, contributions)

    def getUserBalance(self, userId):
        userBal = 0
        for billId in self._billService.allBills:
            bill = self._billService.allBills[billId]
            if userId in bill.contributions:
                userBal = userBal - bill.contributions[userId]
            if userId in bill.paidBy:
                userBal = userBal + bill.paidBy[userId]
        return userBal
