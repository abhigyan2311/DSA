from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self) -> str:
        if self is None:
            return "Nil"
        return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast: return True
        return False
        

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = head.next.next.next

    print(Solution().hasCycle(head))