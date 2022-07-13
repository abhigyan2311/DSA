from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(N), O(N)
    def depth(self, node: TreeNode) -> int:
        if not node: return 0
        leftHeight = self.depth(node.left)
        if leftHeight == -1: return -1
        rightHeight = self.depth(node.right)
        if rightHeight == -1: return -1
        if abs(leftHeight-rightHeight) > 1: return -1
        return 1+max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        height = self.depth(root)
        if height == -1: return False
        return True

