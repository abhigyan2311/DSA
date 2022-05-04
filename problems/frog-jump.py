# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

from math import inf
from typing import *

class Solution:
    # DP - O(n), O(n) + O(n)
    def solve(self, index: int, heights: List[int], dp: List[int]):
        if index == 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        
        left = self.solve(index - 1, heights, dp) + abs(heights[index] - heights[index-1])
        right = inf
        if index > 1:
            right = self.solve(index-2, heights, dp) + abs(heights[index] - heights[index-2])

        minCost = min(left, right)
        dp[index] = minCost
        return minCost

    # def frogJump(self, n: int, heights: List[int]) -> int:
    #     dp = [-1] * (n)
    #     ans = self.solve(n-1, heights, dp)
    #     return ans

    # Tabulation - O(n), O(n)
    def frogJump(self, n: int, heights: List[int]) -> int:
        dp = [-1] * (n)
        dp[0] = 0
        for i in range(1,n):
            fs = dp[i-1] + abs(heights[i] - heights[i-1])
            ss = inf
            if i > 1:
                ss = dp[i-2] + abs(heights[i] - heights[i-2])
            dp[i] = min(fs, ss)
        return dp[n-1]
    
    # Optimal - O(n), O(1)
    def frogJump(self, n: int, heights: List[int]) -> int:
        prev, prev2 = 0, 0
        for i in range(1,n):
            fs = prev + abs(heights[i] - heights[i-1])
            ss = inf
            if i > 1:
                ss = prev2 + abs(heights[i] - heights[i-2])
            cur = min(fs, ss)
            prev2 = prev
            prev = cur
        return prev
        
ans = Solution().frogJump(4, [10,20,30,10])
print(ans)