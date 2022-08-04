# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None

        # return if either p/q found 
        if root == p or root == q:
            return root

        # see if LCA/p/q found in either subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both targets found, combine into LCA & return
        if left and right:
            return root

        # either left/right OR both subtrees are null, so just pass either
        # if LCA/p/q not found in current node & left/right subtree, return None
        return left or right