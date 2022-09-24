from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelorder = []
        if not root:
            return levelorder
        q = deque()
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            levelorder.append(level)
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
