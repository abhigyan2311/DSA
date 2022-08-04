

from cmath import inf


class TreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None


def floorInBST(root, X):
    floor = -1
    while root:
        if root.data == X:
            floor = root.data
            return floor
        if X < root.data:
            root = root.left
        else:
            floor = root.data
            root = root.right
    return floor
