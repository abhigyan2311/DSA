# Definition for a binary tree node.
from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return None

        def validate(node: Optional[TreeNode], lowerBound: int, upperBound: int):
            if not node: return True
            if node.val >= upperBound or node.val <= lowerBound: return False
            left = validate(node.left, lowerBound, node.val)
            right = validate(node.right, node.val, upperBound)
            return left and right
        
        return validate(root, -inf, inf)

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)

ans = Solution().isValidBST(root)
print(ans)
