# https://iq.opengenus.org/reverse-linked-list-alternative-k-nodes/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        if self is None:
            return "Nil"
        return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # Iterative - O(N), O(1)
    def reverseKGroupI(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1: return head
        dummy = ListNode(-1, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: break
            groupNext = kth.next
            
            #Reverse Group
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                curr.next, prev, curr = prev, curr, curr.next

            # Move groupPrev to new group's previous
            groupPrev.next, groupPrev = kth, groupPrev.next
        return dummy.next


    def getKth(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    # Recursive - O(N), O(N/k)
    def reverseKGroupR(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1: return head

        # Check if k group size is valid
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
            
        # Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            curr.next, prev, curr = prev, curr, curr.next
        
        # Solve for remaining list
        head.next = self.reverseKGroupR(curr, k)
        return prev
    
    # Variant 1: Reverse left over nodes as well
    def reverseKGroupV1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1: return head
            
        # Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            if not curr: return prev
            curr.next, prev, curr = prev, curr, curr.next

        # Solve for remaining list
        head.next = self.reverseKGroupV1(curr, k)
        return prev
    
    # Variant 2: Reverse alternate k groups
    def reverseKGroupV2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1: return head

        # Check if k group size is valid
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next

        # Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            curr.next, prev, curr = prev, curr, curr.next
            
        # Point head.next to the remaining list
        head.next = curr

        # Skip next k nodes
        for _ in range(k):
            curr = curr.next

        # Solve for remaining list
        if curr:
            curr.next = self.reverseKGroupV2(curr.next, k)
        return prev


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)
    # head.next.next.next.next.next.next = ListNode(7)
    # head.next.next.next.next.next.next.next = ListNode(8)

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    head2.next.next.next.next.next = ListNode(6)
    head2.next.next.next.next.next.next = ListNode(7)
    head2.next.next.next.next.next.next.next = ListNode(8)

    head3 = ListNode(1)
    head3.next = ListNode(2)
    head3.next.next = ListNode(3)
    head3.next.next.next = ListNode(4)
    head3.next.next.next.next = ListNode(5)
    head3.next.next.next.next.next = ListNode(6)
    head3.next.next.next.next.next.next = ListNode(7)
    head3.next.next.next.next.next.next.next = ListNode(8)

    head4 = ListNode(1)
    head4.next = ListNode(2)
    head4.next.next = ListNode(3)
    head4.next.next.next = ListNode(4)
    head4.next.next.next.next = ListNode(5)
    head4.next.next.next.next.next = ListNode(6)
    head4.next.next.next.next.next.next = ListNode(7)
    head4.next.next.next.next.next.next.next = ListNode(8)
    head4.next.next.next.next.next.next.next.next = ListNode(9)

    # print(Solution().reverseKGroupI(head, 2))
    # print(Solution().reverseKGroupR(head2, 3))
    # print(Solution().reverseKGroupV1(head3, 3))
    # print(Solution().reverseKGroupV2(head4, 3))

    print(Solution().reverseKGroupI(head4, 3))