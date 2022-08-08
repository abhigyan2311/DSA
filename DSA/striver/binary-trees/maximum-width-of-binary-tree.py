# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxWidth = 0
        treeQ = deque()
        treeQ.append((root, 0))
        while treeQ:
            levelMin = treeQ[0][1]
            treeQSize = len(treeQ)
            firstInd, lastInd = 0, 0
            for i in range(treeQSize):
                currNode, currInd = treeQ.popleft()
                currInd -= levelMin
                if i==0: firstInd = currInd
                if i==treeQSize-1: lastInd = currInd
                if currNode.left:
                    treeQ.append((currNode.left, 2*currInd+1))
                if currNode.right:
                    treeQ.append((currNode.right, 2*currInd+2))
            maxWidth = max(maxWidth, lastInd-firstInd+1)
        return maxWidth


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(6)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(7)

ans = Solution().widthOfBinaryTree(root)
print(ans)
