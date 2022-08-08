# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def build(self, preorder: List[int], preStart: int, preEnd: int, inorder: List[int], inStart: int, inEnd: int, inOrderMap: dict) -> TreeNode:
        if preStart > preEnd or inStart > inEnd: return None

        node = TreeNode(preorder[preStart])

        nodeIndex = inOrderMap[node.val]
        numsLeft = nodeIndex - inStart

        node.left = self.build(preorder, preStart+1, preStart+numsLeft, inorder, inStart, nodeIndex-1, inOrderMap)
        node.right = self.build(preorder, preStart+numsLeft+1, preEnd, inorder, nodeIndex+1, inEnd, inOrderMap)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build Inorder Hashmap
        inOrderMap = {}
        for i,val in enumerate(inorder):
            inOrderMap[val] = i
        #Build Tree
        root = self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inOrderMap)
        return root