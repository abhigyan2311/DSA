# https://leetcode.com/problems/powx-n/submissions/
# https://www.youtube.com/watch?v=l0YC3876qxg&t=317&ab_channel=takeUforward

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Approach 1: Brute Force - O(n), O(1)
        # ans = 1
        # sign = 1
        # if n < 0:
        #     sign = -1
        #     n *= sign
        # for _ in range(n):
        #     ans *= x
        # if sign < 0:
        #     return 1/ans
        # return ans

        # Optimized Solution - O(logn)
        ans = 1
        nn = n
        if nn < 0:
            nn = -1 * nn
        while nn > 0:
            if nn % 2 == 1:
                ans = ans * x
                nn = nn - 1
            else:
                x = x * x
                nn = nn/2
        if n < 0:
            ans = 1/ans
        return ans

answer = Solution().myPow(2, -2)
print(answer)