# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(start, end):
            if start == end: return None
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = buildTree(start, mid)
            root.right = buildTree(mid+1, end)
            return root
        return buildTree(0, len(nums))

arr = [-10,-3,0,5,9]
ans = Solution().sortedArrayToBST(arr)
print(ans)