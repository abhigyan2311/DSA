# https://leetcode.com/problems/unique-paths-ii/
# https://youtu.be/TmhpgXScLyY

from typing import List

class Solution:
    # Recursion - O(2^(n*m)), O((m-1)*(n-1)) - path length
    # def solve(self, i: int, j: int, obstacleGrid: List[List[int]]) -> int:
    #     if i == 0 and j == 0 and obstacleGrid[0][0] != 1:
    #         return 1
    #     if i<0 or j<0 or obstacleGrid[i][j] == 1:
    #         return 0
    #     up = self.solve(i-1, j, obstacleGrid)
    #     left = self.solve(i, j-1, obstacleGrid)
    #     ways = up + left
    #     return ways

    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m = len(obstacleGrid)
    #     n = len(obstacleGrid[0])
    #     return self.solve(m-1, n-1, obstacleGrid)
    
    # Recursion + Memoization - O(n*m), O((m-1)*(n-1)) + O(n*m)
    # def solve(self, i: int, j: int, obstacleGrid: List[List[int]], dp: List[List[int]]) -> int:
    #     if i == 0 and j == 0 and obstacleGrid[0][0] != 1:
    #         return 1
    #     if i<0 or j<0 or obstacleGrid[i][j] == 1:
    #         return 0
    #     if dp[i][j] != -1: return dp[i][j]
    #     up = self.solve(i-1, j, obstacleGrid, dp)
    #     left = self.solve(i, j-1, obstacleGrid, dp)
    #     ways = up + left
    #     dp[i][j] = ways
    #     return ways

    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m = len(obstacleGrid)
    #     n = len(obstacleGrid[0])
    #     dp = [[-1]*n for _ in range(m)]
    #     return self.solve(m-1, n-1, obstacleGrid, dp)

    # Iteration + Memoization - O(m*n), O(m*n)
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m = len(obstacleGrid)
    #     n = len(obstacleGrid[0])
    #     dp = [[-1]*n for _ in range(m)]
    #     dp[0][0] = 1
    #     for i in range(m):
    #         for j in range(n):
    #             if i == 0 and j == 0 and obstacleGrid[0][0] != 1:
    #                 dp[0][0] = 1
    #             else:
    #                 up, left = 0,0
    #                 if i>0 and obstacleGrid[i][j] != 1:
    #                     up = dp[i-1][j]
    #                 if j>0 and obstacleGrid[i][j] != 1:
    #                     left = dp[i][j-1]
    #                 dp[i][j] = up+left

    #     return dp[m-1][n-1]
    
    # Iteration + Space Optimization - O(n*m), O(n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0] * n
        
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0 and obstacleGrid[0][0] != 1:
                    curr[j] = 1
                else:
                    up, left = 0,0
                    if i>0 and obstacleGrid[i][j] != 1:
                        up = prev[j]
                    if j>0 and obstacleGrid[i][j] != 1:
                        left = curr[j-1]
                    curr[j] = up+left
            prev = curr

        return prev[n-1]

ans = Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(ans)