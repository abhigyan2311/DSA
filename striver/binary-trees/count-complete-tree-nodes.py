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
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        height = self.getHeight(root)
        
        if height != -1: 
            return (pow(2, height+1) - 1)
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1