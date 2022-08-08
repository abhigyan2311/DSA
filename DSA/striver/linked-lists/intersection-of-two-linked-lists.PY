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
    # O(m+n), O(N)
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     hs = set()
    #     while headA:
    #         hs.add(headA)
    #         headA = headA.next
    #     while headB:
    #         if headB in hs: return headB
    #         headB = headB.next
    #     return None

    # O(2N), O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: return None
        dN1, dN2 = headA, headB

        while dN1 != dN2:
            dN1 = headB if not dN1 else dN1.next
            dN2 = headA if not dN2 else dN2.next
        return dN1



if __name__ == "__main__":
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)

    head2 = ListNode(7)
    head2.next = ListNode(8)
    head2.next.next = head1.next.next.next

    print(Solution().getIntersectionNode(head1, head2))