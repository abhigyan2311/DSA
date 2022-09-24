# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Brute - O(N), O(logN)
    # def count(self, root) -> int:
    #         if root is None:
    #             return 0
    #         left = self.count(root.left)
    #         right = self.count(root.right)
    #         return left+right+1

    #     def countNodes(self, root: Optional[TreeNode]) -> int:
    #         return self.count(root)

    # Optimal - O(logN**2), O(logN)
    # If LH == RH then number of nodes in a complete BT is (2**(H) - 1)
    def findLeftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def findRightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.findLeftHeight(root)
        rightHeight = self.findRightHeight(root)
        if leftHeight == rightHeight:
            return pow(2, leftHeight) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
