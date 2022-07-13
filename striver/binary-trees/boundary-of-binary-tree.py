# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def addLeftBoundary(self, root: TreeNode, res: List[int]):
        curr = root.left
        while curr:
            if not self.isLeaf(curr): res.append(curr.val)
            if curr.left: curr = curr.left
            else: curr = curr.right

    def addLeaves(self, root: TreeNode, res: List[int]):
        if self.isLeaf(root):
            res.append(root.val)
        if root.left: self.addLeaves(root.left, res)
        if root.right: self.addLeaves(root.right, res)

    def addRightBoundary(self, root: TreeNode, res: List[int]):
        curr = root.right
        tmp = []
        while curr:
            if not self.isLeaf(curr): tmp.append(curr.val)
            if curr.right: curr = curr.right
            else: curr = curr.left
        res.extend(reversed(tmp))

    def isLeaf(self, node: TreeNode) -> bool:
        return not node.left and not node.right

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        if not self.isLeaf(root): res.append(root.val)
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)
        return res
