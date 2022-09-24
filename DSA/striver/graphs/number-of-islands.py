import collections
from typing import List

class Solution:
    def __init__(self) -> None:
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # DFS
    # def explore(self, row, col, grid, visited):
    #     if row not in range(len(grid)) or col not in range(len(grid[0])):
    #         return
    #     if (row, col) in visited or grid[row][col] == "0":
    #         return

    #     visited.add((row, col))
    #     for dx, dy in self.directions:
    #         self.explore(row+dx, col+dy, grid, visited)

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     visited = set()
    #     islands = 0

    #     for row in range(rows):
    #         for col in range(cols):
    #             if grid[row][col] == "1" and (row, col) not in visited:
    #                 self.explore(row, col, grid, visited)
    #                 islands += 1
    #     return islands

    # BFS
    def explore(self, row, col, grid, visited):
        dq = collections.deque()
        dq.append((row, col))
        visited.add((row, col))
        while dq:
            currRow, currCol = dq.popleft()
            for dx, dy in self.directions:
                newRow, newCol = currRow+dx, currCol+dy
                if newRow in range(len(grid)) and newCol in range(len(grid[0])) and (newRow, newCol) not in visited and grid[newRow][newCol] == "1":
                    dq.append((newRow, newCol))
                    visited.add((newRow, newCol))

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    self.explore(row, col, grid, visited)
                    islands += 1
        return islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
ans = Solution().numIslands(grid)
print(ans)
        