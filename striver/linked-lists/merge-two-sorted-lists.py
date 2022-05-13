
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Approach 1: O(n1+n2), O(n1+n2)
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     dummy = ListNode()
    #     temp = dummy
    #     while list1 and list2:
    #         if list1.val < list2.val:
    #             temp.next = list1
    #             list1 = list1.next
    #         else:
    #             temp.next = list2
    #             list2 = list2.next
    #         temp = temp.next
    #     if list1: temp.next = list1
    #     if list2: temp.next = list2
    #     return dummy.next

    # Approach 2: In Place Sort - O(n1+n2), O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        if list1.val > list2.val: list1, list2 = list2, list1
        res = list1
        while list1 and list2:
            temp = None
            while list1 and list1.val <= list2.val:
                temp = list1
                list1 = list1.next
            temp.next = list2
            list1, list2 = list2, list1
        return res        

        