from queue import Queue

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def topView(self,root):
        ans = []
        if not root: return ans
        hm = {}
        min_vLevel, max_vLevel = 0, 0
        q = Queue()
        q.put((root, 0))
        while q.qsize() > 0:
            node, vLevel = q.get()
            min_vLevel = min(min_vLevel, vLevel)
            max_vLevel = max(max_vLevel, vLevel)
            if vLevel not in hm:
                hm[vLevel] = node
            if node.left:
                q.put((node.left, vLevel-1))
            if node.right:
                q.put((node.right, vLevel+1))
        for i in range(min_vLevel, max_vLevel+1):
            ans.append(hm[i].data)
        return ans