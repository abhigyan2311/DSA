# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth(self, node: Optional[TreeNode], diameter: List[int]) -> bool:
        if not node: return 0
        leftHeight = self.depth(node.left, diameter)
        rightHeight = self.depth(node.right, diameter)
        diameter[0] = max(diameter[0], leftHeight+rightHeight)
        return 1 + max(leftHeight, rightHeight)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> bool:
        diameter = [-1]
        if not root: return diameter[0]
        self.depth(root, diameter)
        return diameter[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

ans = Solution().diameterOfBinaryTree(root)
print(ans)
        