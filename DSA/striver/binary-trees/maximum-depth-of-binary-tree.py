# Definition for a binary tree node.
from queue import Queue
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative + Levelorder Traversal - O(N), O(N)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        if not root: return maxDepth
        treeQ = Queue()
        treeQ.put((root, 0))
        while treeQ.qsize()>0:
            currNode, level = treeQ.get()
            maxDepth = max(maxDepth, level)
            if currNode.left:
                treeQ.put((currNode.left, level+1))
            if currNode.right:
                treeQ.put((currNode.right, level+1))
        return maxDepth+1
    
    # Recursive - O(N), O(H)
    def recurseDepth(self, node: Optional[TreeNode]) -> int:
        if not node: return 0

        leftTreeHeight = self.recurseDepth(node.left)
        rightTreeHeight = self.recurseDepth(node.right)
        return 1 + max(leftTreeHeight, rightTreeHeight)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurseDepth(root)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

ans = Solution().maxDepth(root)
print(ans)
        