from typing import List

class Solution:
    # # Recursion - O(2^n), O(n)
    # def solve(self, n: int):
    #     if n <= 1:
    #         return n
    #     return self.solve(n-1) + self.solve(n-2)
        
    # DP - O(n), O(n) + O(n)
    # def solve(self, n: int, dp: List[int]):
    #     if n <= 1:
    #         return n
    #     if dp[n] != -1:
    #         return dp[n]
    #     dp[n] = self.solve(n-1, dp) + self.solve(n-2, dp)
    #     return dp[n]
    
    def fib(self, n: int) -> int:
        # Recursion
        # ans = self.solve(n)
        # dp = [-1] * (n+1)
        # ans = self.solve(n, dp)
        if n<2:
            return n
        prev2 = 0
        prev = 1
        for _ in range(2, n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        return prev

ans = Solution().fib(0)
        