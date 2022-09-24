from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def spiralLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelorder = []
        if not root:
            return levelorder
        q = deque()
        q.append(root)
        spiralFlag = True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
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

ans = Solution().spiralLevelOrder(root)
print(ans)
