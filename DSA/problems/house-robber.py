# https://leetcode.com/problems/house-robber/
# https://leetcode.com/problems/house-robber/discuss/1605797/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP

from typing import List

class Solution:
# Recursive(top-down) - O(2^n), O(n)
#     def solve(self, i: int, nums: List[int]) -> int:
#         if i < 0:
#             return 0 
#         return max(self.solve(i-1, nums), nums[i] + self.solve(i-2, nums))

#     def rob(self, nums: List[int]) -> int:
#         nHouses = len(nums)
#         return self.solve(nHouses - 1, nums)
    
# Recursive + Memoization - O(n), O(n) + O(n)
#     def solve(self, i: int, nums: List[int], dp: List[int]) -> int:
#         if i < 0:
#             return 0
#         if dp[i] != -1:
#             return dp[i]
#         cost = max(self.solve(i-2, nums, dp) + nums[i], self.solve(i-1, nums, dp))
#         dp[i] = cost
#         return cost

#     def rob(self, nums: List[int]) -> int:
#         dp = [-1] * len(nums)
#         return self.solve(len(nums) - 1, nums, dp)

# Iterative + Memoization(Bottom Up) - O(n), O(n)
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [-1] * n
    #     dp[0] = nums[0]
    #     for i in range(1, n):
    #         toRob = nums[i]
    #         if i>1: toRob += dp[i-2]
    #         notToRob = dp[i-1]
    #         dp[i] = max(toRob, notToRob)
    #     return dp[n-1]    

# Iterative - O(n), O(1)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        prev2 = 0
        prev = nums[0]
        for i in range(1, n):
            toRob = nums[i]
            if i>1: toRob += prev2
            notToRob = prev
            curr = max(toRob, notToRob)
            prev2, prev = prev, curr
        return prev

ans = Solution().rob([2,7,9,3,1])
print(ans)