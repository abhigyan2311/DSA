from queue import PriorityQueue
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(None)
        curr = dummy
        pq = PriorityQueue()
        for i, node in enumerate(lists):
            if node: pq.put((node.val, i, node))
        while pq.qsize() > 0:
            minNode = pq.get()
            curr.next = minNode[2]
            i = minNode[1]
            curr = curr.next
            if curr.next: pq.put((curr.next.val, i, curr.next))
        return dummy.next
            