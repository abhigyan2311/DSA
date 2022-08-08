# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getHeight(self, node) -> int:
        # countL = countR = 0
        # leftST = node.left
        # rightST = node.right
        # while leftST:
        #     countL += 1
        #     leftST = leftST.left
        # while rightST:
        #     countR += 1
        #     rightST = rightST.right
        # return countL, countR  

        count = 0
        nodeL = node
        nodeR = node
        while nodeL.left and nodeR.right:
            count += 1
            nodeL = nodeL.left
            nodeR = nodeR.right
        if nodeL.left or nodeR.right: return -1
        return count
    
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
        if not root: return 0
        leftHeight = self.findLeftHeight(root)
        rightHeight = self.findRightHeight(root)
        if leftHeight == rightHeight:
            return pow(2, leftHeight) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)