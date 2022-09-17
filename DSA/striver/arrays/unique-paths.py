# https://leetcode.com/problems/unique-paths/
# https://youtu.be/sdE0A2Oxofw

from math import comb
from typing import List

class Solution:
    # Recursion - O(2^(n*m)), O((m-1)*(n-1)) - path length
    # def solve(self, i: int, j: int):
    #     if i == 0 and j == 0:
    #         return 1
    #     if i<0 or j<0:
    #         return 0
    #     return self.solve(i-1, j) + self.solve(i, j-1)

    # def uniquePaths(self, m: int, n: int) -> int:
    #     return self.solve(m-1, n-1)

    # Recursion + Memoization - O(n*m), O((n-1) + (m-1)) + O(n*m)
    # def solve(self, i: int, j: int, dp: List[List[int]]):
    #     if i == 0 and j == 0:
    #         return 1
    #     if i<0 or j<0:
    #         return 0
    #     if dp[i][j] != -1: return dp[i][j]
    #     ways = self.solve(i-1, j, dp) + self.solve(i, j-1, dp)
    #     dp[i][j] = ways
    #     return ways

    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[-1] * n for _ in range(m)]
    #     return self.solve(m-1, n-1, dp)

    # Iteration + Memoization - O(n*m), O(n*m)
    # def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[-1] * n for _ in range(m)]
        # dp[0][0] = 1
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0: dp[0][0] = 1
        #         else:
        #             up, left = 0,0
        #             if i > 0:
        #                 up = dp[i-1][j]
        #             if j > 0:
        #                 left = dp[i][j-1]
        #             ways = up + left
        #             dp[i][j] = ways
        # return dp[m-1][n-1]
    
    # Iteration + Space Optimzation - O(m*n), O(n)
    # def uniquePaths(self, m: int, n: int) -> int:
        # prev = [0] * n
        # for i in range(m):
        #     temp = [0] * n
        #     for j in range(n):
        #         if i == 0 and j == 0: 
        #             temp[0] = 1
        #         else:
        #             up, left = 0,0
        #             if i > 0:
        #                 up = prev[j]
        #             if j > 0:
        #                 left = temp[j-1]
        #             temp[j] = up + left                
        #     prev = temp
        # return prev[n-1]


    def uniquePaths(self, m: int, n: int) -> int:
        N = m+n-2
        r = m-1
        # return comb(N,r)
        res = 1
        for i in range(1, r+1):
            res *= (N-r+i)/i
        return round(res)

ans = Solution().uniquePaths(7, 7)
print(ans)