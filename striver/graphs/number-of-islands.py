import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col = q.popleft()
                directions = [[0,-1], [-1,0], [0,1], [1,0]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and (r, c) not in visit and grid[r][c] == "1":
                        q.append((r, c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        directions = [[0,-1], [-1,0], [0,1], [1,0]]

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != "1" or (r,c) in visit: return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid: return 0
    #     r, c = len(grid), len(grid[0])
    #     visited = [[False for _ in range(c)] for _ in range(r)]

    #     def dfs(i, j):
    #         if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0' or visited[i][j]:
    #             return
    #         visited[i][j] = True
    #         dfs(i + 1, j)
    #         dfs(i - 1, j)
    #         dfs(i, j + 1)
    #         dfs(i, j - 1)

    #     count = 0
    #     for i in range(r):
    #         for j in range(c):
    #             if not visited[i][j] and grid[i][j] == '1':
    #                 dfs(i, j)
    #                 count += 1
    #     return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
ans = Solution().numIslands(grid)
print(ans)
        