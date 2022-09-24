# Definition for a binary tree node.
from collections import deque
from heapq import heappop, heappush
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeEl:
    def __init__(self, node: TreeNode, vLevel=0, hLevel=0) -> None:
        self.node = node
        self.vLevel = vLevel
        self.hLevel = hLevel


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        min_vLevel, max_vLevel = 0, 0
        treeMap = {}
        treeQ = deque()
        treeQ.append(NodeEl(root))
        while treeQ:
            nodeEl = treeQ.popleft()
            node, vLevel, hLevel = nodeEl.node, nodeEl.vLevel, nodeEl.hLevel
            min_vLevel = min(min_vLevel, vLevel)
            max_vLevel = max(max_vLevel, vLevel)
            if vLevel not in treeMap:
                treeMap[vLevel] = {}
            if hLevel not in treeMap[vLevel]:
                treeMap[vLevel][hLevel] = []
            currPQ = treeMap[vLevel][hLevel]
            heappush(currPQ, node.val)

            if node.left:
                leftNodeEl = NodeEl(node.left, vLevel-1, hLevel+1)
                treeQ.append(leftNodeEl)
            if node.right:
                rightNodeEl = NodeEl(node.right, vLevel+1, hLevel+1)
                treeQ.append(rightNodeEl)

        for i in range(min_vLevel, max_vLevel+1):
            currentLevel = []
            for hLevel, pq in treeMap[i].items():
                while pq:
                    currentLevel.append(heappop(pq))
            ans.append(currentLevel)
        return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

ans = Solution().verticalTraversal(root)
print(ans)
