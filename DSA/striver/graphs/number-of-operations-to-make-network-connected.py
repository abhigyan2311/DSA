from collections import defaultdict
from typing import List


class Solution:
    #     def dfs(self, v, adjMatrix, visited):
    #         for adjN in adjMatrix[v]:
    #             if adjN not in visited:
    #                 visited.add(adjN)
    #                 self.dfs(adjN, adjMatrix, visited)

    #     def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    #         if len(connections) < n-1:
    #             return -1

    #         # Build adjMatrix
    #         adjMatrix = defaultdict(list)
    #         for conn in connections:
    #             adjMatrix[conn[0]].append(conn[1])
    #             adjMatrix[conn[1]].append(conn[0])

    #         visited = set()
    #         connected = 0
    #         for v in range(n):
    #             if v not in visited:
    #                 self.dfs(v, adjMatrix, visited)
    #                 connected += 1
    #         return connected-1

    def __init__(self) -> None:
        self.rank = []
        self.parent = []

    def findParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.findParent(x)
        y = self.findParent(y)

        if self.rank[x] < self.rank[y]:
            self.parent[y] = x
        elif self.rank[y] < self.rank[x]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        self.rank = [0]*n
        self.parent = [i for i in range(n)]

        for x, y in connections:
            self.union(x, y)

        conn = 0
        for i in range(n):
            if self.parent[i] == i:
                conn += 1
        return conn - 1


ans = Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]])
print(ans)
