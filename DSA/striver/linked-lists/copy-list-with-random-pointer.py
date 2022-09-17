
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self) -> str:
        if self is None:
            return "Nil"
        return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # Hashmap - O(2N), O(N)
        #         if not head: return None
        #         hm = dict()
        #         # Create main nodes without any next/random pointers
        #         curr = head
        #         while curr:
        #             hm[curr] = ListNode(curr.val)
        #             curr = curr.next
        #         # Assign them next and random pointers
        #         curr = head
        #         while curr:
        #             hm[curr].next = hm.get(curr.next)
        #             hm[curr].random = hm.get(curr.random)
        #             curr = curr.next

        #         return hm.get(head)

        # Optimal - O(3N), O(1)
        if not head:
            return None

        # Insert duplicate nodes next to curr node
        curr = head
        while curr:
            nn = Node(curr.val, curr.next)
            curr.next = nn
            curr = curr.next.next

        # Set the random pointers for the duplicate nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Separate two lists
        dummy = Node(-1, head.next)
        curr = head.next
        while curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return dummy.next


if __name__ == "__main__":
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)

    head1.random = head1.next.next.next
    head1.next.random = head1
    head1.next.next.next.random = head1.next

    print(Solution().copyRandomList(head1))
