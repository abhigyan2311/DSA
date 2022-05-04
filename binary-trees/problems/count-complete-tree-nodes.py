from queue import Queue
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val) -> None:
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
    
    def levelorder(self, root):
        levelorder = []
        if root is None: return levelorder
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            level = []
            for _ in range(size):
                node = q.get()
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
                level.append(node.val)
            levelorder.append(level)
        return levelorder
        
class Solution:
    def count(self, root) -> int:
        if root is None:
            return 0
        left = self.count(root.left)
        right = self.count(root.right)
        return left+right+1

    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.count(root)

root = TreeNode(10)
root.insert(5)
root.insert(15)
root.insert(1)
root.insert(6)
root.insert(12)
root.insert(16)
print(root.levelorder(root))
print(Solution().countNodes(root))