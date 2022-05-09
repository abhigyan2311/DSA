from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iterative - O(N), O(1)
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     current = head
    #     next = None
    #     while current:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     head = prev
    #     return prev

    # Recursive - O(N), O(N)
    def _reverse(self, node, prev=None):
        if not node:
            return prev
        nn = node.next
        node.next = prev
        return self._reverse(nn, node)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse(head)