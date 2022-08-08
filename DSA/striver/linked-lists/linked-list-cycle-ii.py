from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self) -> str:
        if self is None:
            return "Nil"
        return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None
        slow = fast = head
        cycleExists = False
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                cycleExists = True
                break
        if not cycleExists: return None
        fast = head
        while slow is not fast:
            slow, fast = slow.next, fast.next
        
        return slow
        

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = head.next.next.next

    print(Solution().hasCycle(head))