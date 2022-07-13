# Definition for a binary tree node.
from math import inf
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMaxSum(self, node, maxSumm: List[int]) -> bool:
        if not node: return 0

        left = max(0, self.findMaxSum(node.left, maxSumm))
        right = max(0, self.findMaxSum(node.right, maxSumm))

        maxSumm[0] = max(maxSumm[0], left+right+node.val)
        return node.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> bool:
        maxSumm = -inf

        def findMaxSum(node):
            nonlocal maxSumm

            if not node: return 0

            left = max(0, findMaxSum(node.left))
            right = max(0, findMaxSum(node.right))

            maxSumm = max(maxSumm, node.val+left+right)
            return node.val + max(left,right)

        findMaxSum(root)
        return maxSumm
