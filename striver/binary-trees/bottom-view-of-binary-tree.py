from queue import Queue
from typing import Optional

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def bottomView(self, root: Optional[Node]):
        ans = []
        if not root: return ans
        hm = {}
        min_vLevel, max_vLevel = 0, 0
        q = Queue()
        q.put((root, 0))
        while q.qsize() > 0:
            node, vLevel = q.get()
            min_vLevel = min(min_vLevel, vLevel)
            max_vLevel = max(max_vLevel, vLevel)
            hm[vLevel] = node.data
            if node.left:
                q.put((node.left, vLevel-1))
            if node.right: 
                q.put((node.right, vLevel+1))
        for i in range(min_vLevel, max_vLevel+1):
            ans.append(hm[i])
        return ans


root = Node(1)
root.left = Node(3)
root.right = Node(2)

ans = Solution().bottomView(root)
print(ans)
