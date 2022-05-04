# https://leetcode.com/problems/climbing-stairs
# https://youtu.be/mLfjzJsN8us
# https://youtu.be/Y0lT9Fck7qI

from typing import List

class Solution:
    # Brute Force Recursion - O(n^2), O(n)
    # def solve(self, n: int):
    #     if n == 0 or n == 1:
    #         return 1
    #     left = self.solve(n-1)
    #     right = self.solve(n-2)
    #     return left+right

    # def climbStairs(self, n: int) -> int:
    #     ways = self.solve(n)
    #     return ways
    
    # DP - O(n^2), O(n) + O(n)
    # def solve(self, n: int, dp: List[int]):
    #     if n == 0 or n == 1:
    #         return 1

    #     left, right = 0, 0
    #     if dp[n-1] != -1:
    #         left = dp[n-1]
    #     else:
    #         left = self.solve(n-1, dp)
    #         dp[n-1] = left

    #     if dp[n-2] != -1:
    #         right = dp[n-2]
    #     else:
    #         right = self.solve(n-2, dp)
    #         dp[n-2] = right

    #     return left+right

    # def climbStairs(self, n: int) -> int:
    #     dp = [-1] * n
    #     ways = self.solve(n, dp)
    #     return ways

    # Optimal - O(n), O(1)
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for _ in range(n-1):
            one, two = one + two, one
        return one   

ans = Solution().climbStairs(3)
print(ans)