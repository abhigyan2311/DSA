# Definition for a binary tree node.
from math import inf
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> bool:
        maxxSumm = -inf

        def findMaxSum(node):
            nonlocal maxxSumm
            if not node:
                return 0
            left = max(0, findMaxSum(node.left))
            right = max(0, findMaxSum(node.right))
            maxxSumm = max(maxxSumm, left+node.val+right)
            return node.val+max(left, right)

        findMaxSum(root)
        return maxxSumm
