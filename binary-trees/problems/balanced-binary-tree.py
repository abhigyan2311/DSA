# https://leetcode.com/problems/balanced-binary-tree/
# https://youtu.be/Yt50Jfbd8Po

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert(self, val) -> None:
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            else:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

class Solution:
    # O(N), O(N)
    def checkHeight(self, root) -> bool:
        if root == None:
            return 0
        left = self.checkHeight(root.left)
        if left == -1: return -1
        right = self.checkHeight(root.right)
        if right == -1: return -1

        if abs(left-right) > 1: return -1
        return max(left,right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res =  self.checkHeight(root)
        if res == -1: return False
        return True

root = TreeNode(10)
root.insert(5)
root.insert(15)
root.insert(1)
root.insert(6)
root.insert(12)
root.insert(16)
ans = Solution().isBalanced(root)
print(ans)
    