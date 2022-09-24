
# Definition for singly-linked list.
from heapq import heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        minHeap = []
        for i, node in enumerate(lists):
            if node:
                heappush(minHeap, (node.val, i, node))
        while minHeap:
            nodeVal, i, node = heappop(minHeap)
            temp.next = node
            temp = temp.next
            if node.next:
                heappush(minHeap, (node.next.val, i, node.next))
        return dummy.next
