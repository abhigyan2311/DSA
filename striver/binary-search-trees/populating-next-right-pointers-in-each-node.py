# Definition for a Node.
from collections import deque
from queue import Queue
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        q = Queue()
        q.put(root)
        while q.qsize() > 0:
            size = q.qsize()
            level = []
            for _ in range(size):
                prevNode = q.get()
                level.append(prevNode)
                if prevNode.left: q.put(prevNode.left)
                if prevNode.right: q.put(prevNode.right)
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        
        # BFS - O(N), O(N)
        if not root: return None
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                q.append(curr.left)
                q.append(curr.right)
        
        # DFS
        if not root: return None
        st = [root]
        while st:
            curr = st.pop()
            if curr.left and curr.right:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                st.append(curr.right)
                st.append(curr.left)
        
        # Recusrsive
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        
        # Optimized BFS
        head = root
        while root:
            curr, root = root, root.left
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                    if curr.next: curr.right.next = curr.next.left
                else: break
                curr = curr.next
        return head
            

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

ans = Solution().connect(root)
print(ans)
        