from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0: return 0
        minsPassed = 0
        rotten = deque()
        freshOranges = 0
        
        # Count total non-empty cells and also count initial rotten orranges
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: freshOranges += 1
                if grid[i][j] == 2: rotten.append((i, j))

        while rotten and freshOranges > 0:
            minsPassed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x+dx, y+dy
                    if xx<0 or xx==m or yy<0 or yy==n: continue
                    if grid[xx][yy]==0 or grid[xx][yy]==2: continue

                    grid[xx][yy] = 2
                    freshOranges -= 1
                    rotten.append((xx, yy))
        
        return minsPassed if freshOranges == 0 else -1

ans = Solution().orangesRotting([[1],[2],[1],[2]])
print(ans)