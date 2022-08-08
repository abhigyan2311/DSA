from queue import Queue
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelorder = []
        if not root: return levelorder
        q = Queue()
        q.put(root)
        spiralFlag = True
        while not q.empty():
            size = q.qsize()
            level = []
            for _ in range(size):
                node = q.get()
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
                level.append(node.val)
            if spiralFlag:
                levelorder.append(level)
            else:
                levelorder.append(level[::-1])
            spiralFlag = not spiralFlag
            
        return levelorder

root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(10)
root.left.right = TreeNode(12)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

ans = Solution().levelOrder(root)
print(ans)