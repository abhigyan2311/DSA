# https://youtu.be/beOCN7G4h-M

from collections import defaultdict
from typing import List


class UF:
    def __init__(self, stones) -> None:
        self.parent = dict()
        self.rank = defaultdict(int)
        self.count = 0

        for stone in stones:
            row = -(stone[0]+1)
            col = stone[1]+1
            self.parent[row] = row
            self.parent[col] = col
        self.count = len(self.parent)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.count -= 1

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UF(stones)
        for stone in stones:
            row = -(stone[0]+1)
            col = stone[1]+1
            uf.union(row, col)
        return len(stones) - uf.count


stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
ans = Solution().removeStones(stones)
print(ans)
