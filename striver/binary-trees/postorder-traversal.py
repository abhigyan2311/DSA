# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorder(self, curr: Optional[TreeNode], ans: List[int]):
        if not curr: return
        self.postorder(curr.left, ans)
        self.postorder(curr.right, ans)
        ans.append(curr.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.postorder(root, ans)
        return ans
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     ans = []
    #     if not root: return ans
    #     st1, st2 = [], []
    #     st1.append(root)
    #     while st1:
    #         root = st1.pop()
    #         st2.append(root)
    #         if root.left: st1.append(root.left)
    #         if root.right: st1.append(root.right)
    #     while st2:
    #         ans.append(st2.pop().val)
    #     return ans
    
    # LEFT RIGHT ROOT
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return ans
        st = []
        curr = root
        while st or curr:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                temp = st[-1].right
                if temp:
                    curr = temp
                else:
                    temp = st.pop()
                    ans.append(temp.val)
                    while st and temp == st[-1].right:
                        temp = st.pop()
                        ans.append(temp.val)
        return ans

            