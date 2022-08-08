from typing import List, Optional

# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

def traverse(node: Optional[Node], level: int, ans: List[int]):
    if not node: return
    if len(ans) == level:
        ans.append(node.data)
    traverse(node.left, level+1, ans)
    traverse(node.right, level+1, ans)

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    ans = []
    traverse(root, 0, ans)
    return ans