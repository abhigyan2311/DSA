from typing import Optional

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

class Solution:
    def mergeTwoLists(self, headA: Optional[Node], headB: Optional[Node]) -> Optional[Node]:
        dummy = Node(-1)
        temp = dummy

        # Traverse both linked lists
        while headA and headB:
            if headA.data < headB.data:
                temp.bottom = headA
                temp = temp.bottom
                headA = headA.bottom
            else:
                temp.bottom = headB
                temp = temp.bottom
                headB = headB.bottom
        
        # If there is some list non empty then append to temp
        if headA: temp.bottom = headA
        if headB: temp.bottom = headB

        # Return the dummy's bottom pointer as it is holding our merged list
        return dummy.bottom

    def flatten(self, root: Optional[Node]) -> Optional[Node]:
        if not root or not root.next:
            return root
        
        # Recurse till right list
        root.next = self.flatten(root.next)

        # Merge the current and right list
        root = self.mergeTwoLists(root, root.next)

        return root

