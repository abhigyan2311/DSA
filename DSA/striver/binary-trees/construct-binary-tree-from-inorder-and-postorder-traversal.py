# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def build(self, postorder: List[int], postStart: int, postEnd: int, inorder: List[int], inStart: int, inEnd: int, inOrderMap: dict) -> TreeNode:
        if postStart > postEnd or inStart > inEnd: return None

        node = TreeNode(postorder[postEnd])

        nodeIndex = inOrderMap[node.val]
        numsLeft = nodeIndex - inStart

        node.left = self.build(postorder, postStart, postStart+numsLeft-1, inorder, inStart, nodeIndex-1, inOrderMap)
        node.right = self.build(postorder, postStart+numsLeft, postEnd-1, inorder, nodeIndex+1, inEnd, inOrderMap)
        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Build Inorder Hashmap
        inOrderMap = {}
        for i,val in enumerate(inorder):
            inOrderMap[val] = i
        #Build Tree
        root = self.build(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1, inOrderMap)
        return root