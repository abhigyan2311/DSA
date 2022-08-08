# https://leetcode.com/problems/unique-paths-ii/
# https://youtu.be/TmhpgXScLyY

from math import inf
from typing import List

class Solution:
    # Recursion - O(2^(m*n)), O((m-1)*(n-1)) - path length
    # def solve(self, i: int, j: int, grid: List[List[int]]) -> int:
    #     if i==0 and j==0: return grid[i][j]
    #     if i<0 or j<0: return inf

    #     up = grid[i][j] + self.solve(i-1, j, grid)
    #     left = grid[i][j] + self.solve(i, j-1, grid)
    #     return min(left, up)

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     return self.solve(m-1, n-1, grid)
    
    # Recursion + Memoization - O(m*n), O((m-1)*(n-1)) + O(m*n)
    # def solve(self, i: int, j: int, grid: List[List[int]], dp: List[List[int]]) -> int:
    #     if i==0 and j==0: return grid[i][j]
    #     if i<0 or j<0: return inf
    #     if dp[i][j] != -1: return dp[i][j]

    #     up = grid[i][j] + self.solve(i-1, j, grid, dp)
    #     left = grid[i][j] + self.solve(i, j-1, grid, dp)
    #     dp[i][j] = min(left, up)
    #     return dp[i][j]

    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     dp = [[-1]*n for _ in range(m)]
    #     return self.solve(m-1, n-1, grid, dp)

    # Iteration + Memoization - O(m*n), O(m*n)
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     dp = [[0]*n for _ in range(m)]
    #     dp[0][0] = grid[0][0]
    #     for i in range(m):
    #         for j in range(n):
    #             if i==0 and j==0: dp[i][j] = grid[i][j]
    #             else:
    #                 up, left = inf, inf
    #                 if i>0:
    #                     up = grid[i][j] + dp[i-1][j]
    #                 if j>0:
    #                     left = grid[i][j] + dp[i][j-1]
    #                 dp[i][j] = min(up, left)
                    
    #     return dp[m-1][n-1]

    # Iteration + Space Optimazation - O (m*n), O(n)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = [0]*n
        
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i==0 and j==0: curr[j] = grid[i][j]
                else:
                    up, left = inf, inf
                    if i>0:
                        up = grid[i][j] + prev[j]
                    if j>0:
                        left = grid[i][j] + curr[j-1]
                    curr[j] = min(up, left)
            prev = curr
                    
        return prev[n-1]

ans = Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(ans)