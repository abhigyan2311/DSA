# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorder(self, root: Optional[TreeNode], res: List[int]):
        if not root: return
        res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preorder(root, res)
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return ans
        st = []
        st.append(root)
        while st:
            root = st.pop()
            ans.append(root.val)
            if root.right: st.append(root.right)
            if root.left: st.append(root.left)
        return ans


