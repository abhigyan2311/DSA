# Definition for a binary tree node.
from math import inf
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        i = 0
        def buildBST(bound: int):
            nonlocal i
            if i == len(preorder) or preorder[i] > bound: return None
            root = TreeNode(preorder[i])
            i += 1
            root.left = buildBST(root.val)
            root.right = buildBST(bound)
            return root
        
        return buildBST(inf)

        
