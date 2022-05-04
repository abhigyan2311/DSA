# https://youtu.be/GrMBfJNk_NY
# https://bit.ly/3q5rlUY

from typing import List

class Solution:
# Recursive - O(2^n), O(n)
    # def solve(self, i: int, nums: List[int]) -> int:
        # if i == 0: return nums[i]
        # if i < 0: return 0
        # return max(self.solve(i-2, nums) + nums[i], self.solve(i-1, nums))

    # def maximumNonAdjacentSum(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     return self.solve(n-1, nums)

# Recursion + Memoization - O(n), O(n) + O(n)
#     def solve(self, i: int, nums: List[int], dp: List[int]) -> int:
#         if i == 0: return nums[i]
#         if i < 0: return 0
#         if dp[i] != -1: return dp[i]
#         dp[i] = max(self.solve(i-2, nums, dp) + nums[i], self.solve(i-1, nums, dp))
#         return dp[i]

#     def maximumNonAdjacentSum(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [-1] * n
#         return self.solve(n-1, nums, dp)

# Iteration + Memoization - O(n), O(n)
#     def maximumNonAdjacentSum(self, nums: List[int]) -> int:
#             n = len(nums)
#             if n == 1: return nums[0]
#             dp = [-1] * n
#             dp[0] = nums[0]
#             for i in range(1, n):
#                 pick = nums[i]
#                 if i>1: pick += dp[i-2]
#                 notPick = dp[i-1]
#                 dp[i] = max(pick, notPick)
#             return dp[n-1]
            
# Iteration - O(n), O(1)
    def maximumNonAdjacentSum(self, nums: List[int]) -> int:
            n = len(nums)
            if n == 1: return nums[0]
            prev2 = 0
            prev = nums[0]
            for i in range(1, n):
                pick = nums[i]
                if i > 1: pick += prev2
                notPick = prev
                curr = max(pick, notPick)
                prev2, prev = prev, curr
            return prev

ans = Solution().maximumNonAdjacentSum([5, 6, 6])
print(ans)