#User function Template for python3
from math import inf


class Node:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None

def findPreSuc(root, pre, suc, key):
    root2 = root
    while root:
        if key >= root.key:
            root = root.right
        else:
            suc[0] = root
            root = root.left
    
    while root2:
        if key < root2.key:
            root2 = root2.left
        else:
            pre[0] = root2
            root2 = root2.right
