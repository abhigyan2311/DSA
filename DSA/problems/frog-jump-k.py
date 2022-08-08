# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

from math import inf
from typing import *

class Solution:
    # Brute Force - O(n^k), O(n)
    # def solve(self, index: int, heights: List[int], k: int):
    #     if index == 0:
    #         return 0
        
    #     minCost = inf
    #     for j in range(1,k+1):
    #         if index - j >= 0:
    #             jump = self.solve(index-j, heights, k) + abs(heights[index]-heights[index-j])
    #             minCost = min(jump, minCost)
    #         else:
    #             break

    #     return minCost

    # def frogJump(self, n: int, heights: List[int], k: int) -> int:
    #     ans = self.solve(n-1, heights, k)
    #     return ans

    # DP - O(n*k), O(n)
    # def solve(self, index: int, heights: List[int], k: int, dp: List[int]) -> int:
    #     if index == 0:
    #         return 0
    #     if dp[index] != -1: return dp[index]

    #     minCost = inf
    #     for j in range(1,k+1):
    #         if index - j >= 0:
    #             jump = self.solve(index-j, heights, k, dp) + abs(heights[index]-heights[index-j])
    #             minCost = min(jump, minCost)
    #         else:
    #             break
    #     dp[index] = minCost        
    #     return minCost

    # def frogJump(self, n: int, heights: List[int], k: int) -> int:
    #     dp = [-1] * n
    #     ans = self.solve(n-1, heights, k, dp)
    #     return ans

    # Tabulation - O(n*k), O(n)
    def frogJump(self, n: int, heights: List[int], k: int) -> int:
        dp = [-1] * (n)
        dp[0] = 0
        minCost = inf
        for i in range(1,n):
            for j in range(1,k+1):
                if i-j >= 0:
                    cost = dp[i-j] + abs(heights[i] - heights[i-j])
                    minCost = min(cost, minCost)
            dp[i] = minCost    
        return dp[n-1]
    
    # Optimal - O(n), O(1)
    # def frogJump(self, n: int, heights: List[int]) -> int:
    #     prev, prev2 = 0, 0
    #     for i in range(1,n):
    #         fs = prev + abs(heights[i] - heights[i-1])
    #         ss = inf
    #         if i > 1:
    #             ss = prev2 + abs(heights[i] - heights[i-2])
    #         cur = min(fs, ss)
    #         prev2 = prev
    #         prev = cur
    #     return prev
        
ans = Solution().frogJump(4, [10,20,30,20], 2)
print(ans)