# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative - O(N), O(N)
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         st = []
#         res = []
#         while root or st:
#             while root:
#                 st.append(root)
#                 root = root.left
#             root = st.pop()
#             res.append(root.val)
#             root = root.right
#         return res

    # Recursive - O(N), O(N)
#     def inorder(self, node: Optional[TreeNode], res: List[int]) -> int:
#         if not node: return
#         self.inorder(node.left, res)
#         res.append(node.val)
#         self.inorder(node.right, res)
    
#     def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         self.inorder(root, res)
#         return res

    # Morris Traversal - O(N), O(1)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        ans = []
        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr
                    ans.append(curr.val)
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return ans

