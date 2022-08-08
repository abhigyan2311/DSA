# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
#Preorder - Root Left Right
class Solution:
    # Recursive - O(N), O(N)
    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     prev = None
    #     def flat(node: Optional[TreeNode]) -> None:
    #         nonlocal prev
    #         if not node: return
    #         flat(node.right)
    #         flat(node.left)
    #         node.right = prev
    #         node.left = None
    #         prev = node
    #     flat(root)
    
    # Iterative - O(N), O(N)
    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     if not root: return None
    #     st = [root]
    #     while st:
    #         curr = st.pop()
    #         if curr.right: st.append(curr.right)
    #         if curr.left: st.append(curr.left)
    #         if st: curr.right = st[-1]
    #         curr.left = None

    # Morris - O(N), O(1)
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return None
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)

Solution().flatten(root)

        