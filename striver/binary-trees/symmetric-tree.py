# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def symmetricCheck(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left or not right:
            return left == right
        
        if left.val != right.val: return False
        
        outPair = self.symmetricCheck(left.left, right.right)
        inPair = self.symmetricCheck(left.right, right.left)
        return outPair and inPair

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.symmetricCheck(root.left, root.right)
        