class BinaryTreenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def traverse(self, node):
        if not node: return

        childSum = 0
        if node.left: childSum += node.left.data
        if node.right: childSum += node.right.data

        if childSum > node.data:
            node.data = childSum
        else:
            if node.left: node.left.data = node.data
            if node.right: node.right.data = node.data
        
        self.traverse(node.left)
        self.traverse(node.right)

        tot = 0
        if node.left: tot += node.left.data
        if node.right: tot += node.right.data
        if node.left or node.right: node.data = tot

def changeTree(root): 
    BinaryTreenode().traverse(root)