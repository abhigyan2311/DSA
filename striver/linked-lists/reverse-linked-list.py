from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iterative - O(N), O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            #1
            # next = curr.next
            # curr.next = prev
            # prev = curr
            # curr = next

            #2
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev

    # Recursive - O(N), O(N)
    def _reverse(self, curr, prev=None):
        if not curr: return prev
        nn = curr.next
        curr.next = prev
        return self._reverse(nn, curr)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse(head)