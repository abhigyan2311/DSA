
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        if not self: return "Nil"
        return "{} -> {}".format(self.val, repr(self.next))
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Brute Force - O(k*N), O(1)
        # if not head or not head.next: return head
        # for _ in range(k):
        #     temp = head
        #     while temp.next.next:
        #         temp = temp.next
        #     end = temp.next
        #     temp.next = None
        #     end.next = head
        #     head = end

        # Optimal - O(N), O(1)
        if not head or k==0: return head

        # Compute length
        length, curr = 1, head
        while curr.next:
            curr = curr.next
            length += 1
        
        # Compute k
        k = k%length
        if k == 0: return head

        # Set last node's next to first node
        curr.next = head

        # Traverse till preK and set head to next node and set next pointer to None
        preK = length - k
        tempNode = head
        for _ in range(preK-1):
            tempNode = tempNode.next
        head = tempNode.next
        tempNode.next = None

        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    print(head)
    print(Solution().rotateRight(head, 2))