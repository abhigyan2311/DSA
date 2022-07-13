class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def mirrorNode(self, node):
        if not node: return
        node.left, node.right = node.right, node.left
        self.mirrorNode(node.left)
        self.mirrorNode(node.right)
        
    def mirror(self,root):
        self.mirrorNode(root)