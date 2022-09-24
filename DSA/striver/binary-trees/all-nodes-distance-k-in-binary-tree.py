# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def markParents(self, root: TreeNode, parentMap: dict):
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr.left:
                parentMap[curr.left] = curr
                q.append(curr.left)
            if curr.right:
                parentMap[curr.right] = curr
                q.append(curr.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Mark Parents
        parentMap = {}
        self.markParents(root, parentMap)

        visited = set()
        q = deque()
        q.append(target)
        visited.add(target)
        currLevel = 0
        while q:
            if currLevel == k:
                break
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left and curr.left not in visited:
                    q.append(curr.left)
                    visited.add(curr.left)
                if curr.right and curr.right not in visited:
                    q.append(curr.right)
                    visited.add(curr.right)
                if curr in parentMap and parentMap[curr] not in visited:
                    q.append(parentMap[curr])
                    visited.add(parentMap[curr])
            currLevel += 1
        res = []
        while q:
            curr = q.popleft()
            res.append(curr.val)
        return res


root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

ans = Solution().distanceK(root, root.left, 2)
print(ans)
