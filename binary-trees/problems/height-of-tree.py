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
    # Recursion - O(n), O(n)
    def solve(self, root) -> int:
        if root is None:
            return 0
        left = self.solve(root.left)
        right = self.solve(root.right)
        return max(left, right) + 1

    def calculateHeight(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)

root = TreeNode(10)
root.insert(5)
root.insert(15)
root.insert(1)
root.insert(6)
root.insert(12)
root.insert(16)
print(Solution().calculateHeight(root))