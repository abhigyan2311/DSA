# https://leetcode.com/problems/diameter-of-binary-tree/
# https://youtu.be/Rezetez59Nk

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
    def findDiameter(self, root, diameter) -> bool:
        if root == None:
            return 0
        left = self.findDiameter(root.left, diameter)
        right = self.findDiameter(root.right, diameter)
        diameter[0] = max(diameter[0], left+right)
        return max(left,right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> bool:
        diameter = [0]
        self.findDiameter(root, diameter)
        return diameter[0]

root = TreeNode(10)
root.insert(5)
root.insert(15)
root.insert(1)
root.insert(6)
root.insert(12)
root.insert(16)
ans = Solution().diameterOfBinaryTree(root)
print(ans)
    