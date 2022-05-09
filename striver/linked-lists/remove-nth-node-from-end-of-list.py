from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # Approach 1: O(2N), O(1)
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     counter = 0
    #     node = head
    #     while node:
    #         node = node.next
    #         counter += 1
    #     startIndex = counter - n
    #     if startIndex == 0:
    #         head = head.next
    #         return head
    #     counter = 0
    #     node = head
    #     while node:
    #         if counter == startIndex-1:
    #             node.next = node.next.next
    #             break
    #         node = node.next
    #         counter += 1
    #     return head

    # Optimal - O(N), O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next

        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().removeNthFromEnd(head, 2))
        


        