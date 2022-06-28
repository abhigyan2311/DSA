from typing import Optional

class Node:
    def __init__(self, val=0, next=None, bottom=None):
        self.val=val
        self.next=next
        self.bottom=bottom

class Solution:
    def mergeTwoLists(self, headA: Optional[Node], headB: Optional[Node]) -> Optional[Node]:
        dummy = Node(-1)
        temp = dummy

        # Traverse both linked lists
        while headA and headB:
            if headA.val <= headB.val:
                temp.bottom = headA
                headA = headA.bottom
                temp = temp.bottom
            else:
                temp.bottom = headB
                headB = headB.bottom
                temp = temp.bottom
        
        # If there is some list non empty then append to temp
        if headA: temp.bottom = headA
        if headB: temp.bottom = headB

        # Return the dummy's bottom pointer as it is holding our merged list
        return dummy.bottom

    def flatten(self, root: Optional[Node]) -> Optional[Node]:
        # Base Case
        if not root or not root.next:
            return root
        # Recurse till right list
        root.next = self.flatten(root.next)
        
        # Merge the current and right list
        root = self.mergeTwoLists(root, root.next)
        
        return root


root = Node(5)
n1 = Node(7)
n2 = Node(8)
n3 = Node(30)
n1.bottom = n2
n2.bottom = n3
n4 = Node(10)
n5 = Node(20)
n4.bottom = n5
root.next = n4

n6 = Node(19)
n7 = Node(22)
n8 = Node(50)
n6.bottom = n7
n7.bottom = n8
n4.next = n6

n9 = Node(28)
n10 = Node(35)
n11 = Node(40)
n12 = Node(45)
n9.bottom = n10
n10.bottom = n11
n11.bottom = n12
n6.next = n9


def printList(node):
    while node:
        print(node.val, end= " ")
        node = node.bottom

printList(Solution().flatten(root))
