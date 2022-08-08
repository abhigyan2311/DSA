# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def findPath(self, node, target, ans):
        if not node: return False

        ans.append(node.val)

        if node.val == target: return True

        if self.findPath(node.left, target, ans) or self.findPath(node.right, target, ans):
            return True
        
        ans.pop()
        return False

    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        self.findPath(A, B, ans)
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

ans = Solution().solve(root, 5)
print(ans)


