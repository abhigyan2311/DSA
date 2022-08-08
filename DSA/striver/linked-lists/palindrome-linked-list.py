from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        if not self: return "Nil"
        return "{} -> {}".format(self.val, repr(self.next))

# O(N/2) + O(N/2) + O(N/2), O(1)
class Solution:
    def reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = node
        while curr:
            curr.next, prev, curr= prev, curr, curr.next
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Check for edge cases
        if not head or not head.next: return True
        
        # Traverse the list using slow and fast pointer to find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        # Reverse the list after middle pointer
        slow.next = self.reverse(slow.next)

        # Check both the halves for equality
        slow = slow.next
        dummy = head
        while slow:
            if slow.val != dummy.val: return False
            slow, dummy = slow.next, dummy.next
        return True

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    print(Solution().isPalindrome(head))
        