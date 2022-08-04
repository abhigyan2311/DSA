from collections import deque
from math import inf
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rotten = deque()
        freshOranges = 0
        minPassed = 0

        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: freshOranges += 1
                elif grid[row][col] == 2: rotten.append((row, col))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while rotten and freshOranges > 0:
            minPassed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in directions:
                    xx, yy = x+dx, y+dy
                    if xx not in range(rows) and yy not in range(cols): continue
                    if grid[xx][yy]==0 or grid[xx][yy]==2: continue
                    grid[xx][yy] = 2
                    rotten.append((xx,yy))
                    freshOranges -= 1
        return minPassed if freshOranges == 0 else -1



ans = Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
# [-1, 4, -1, 2, 2]
print(ans)