from email.headerregistry import Group
from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from controllers.bill_controller import BillController

from services.bill_service import BillService
from services.group_service import GroupService
from services.user_service import UserService


userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('user1', 'abhigyan')
user2 = userController.addUser('user2', 'aalekh')
user3 = userController.addUser('user3', 'shrey')
user4 = userController.addUser('user4', 'akshay')
user5 = userController.addUser('user5', 'devansh')

members = [user1, user2, user3, user4, user5]
group1 = groupController.addGroup('group1', 'Hello World', members)

paidBy = {'user1': 200, 'user2': 100, 'user3': 50, 'user4': 50, 'user5': 100}
contributions = {'user1': 100, 'user2': 100,
                 'user3': 100, 'user4': 100, 'user5': 100}

bill1 = billController.addBill(
    'bill1', 'Electricity Bill', 'group1', 500, paidBy, contributions)

balance = billController.getUserBalance('user1')
print(balance)
