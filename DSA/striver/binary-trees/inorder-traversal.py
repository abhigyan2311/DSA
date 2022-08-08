# Definition for a binary tree node.
from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            res.append(root.val)
            root = root.right
        return res

    
    # def inorder(self, node: Optional[TreeNode], res: List[int]) -> int:
    #     if not node: return
    #     self.inorder(node.left, res)
    #     res.append(node.val)
    #     self.inorder(node.right, res)
        
    
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #     self.inorder(root, res)
    #     return res