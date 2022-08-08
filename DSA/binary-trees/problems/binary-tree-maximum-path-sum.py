# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# https://youtu.be/Rezetez59Nk

from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert(self, val) -> None:
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

class Solution:
    # O(N), O(N)
    def findMaxSum(self, root, maxi) -> bool:
        if root == None:
            return 0
        left = max(0, self.findMaxSum(root.left, maxi))
        right = max(0, self.findMaxSum(root.right, maxi))
        maxi[0] = max(maxi[0], left+right+root.val)
        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> bool:
        maxi = [-inf]
        self.findMaxSum(root, maxi)
        return maxi[0]

root = TreeNode(-3)
# root.insert(5)
# root.insert(15)
# root.insert(1)
# root.insert(6)
# root.insert(12)
# root.insert(16)
ans = Solution().maxPathSum(root)
print(ans)
    