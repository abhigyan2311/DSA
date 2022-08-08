from typing import List

class Solution:
# Recursive(top-down) - O(2^n), O(n)
#     def solve(self, i: int, nums: List[int]) -> int:
#         if i < 0:
#             return 0
#         toPick = self.solve(i-2, nums) + nums[i]
#         notToPick = self.solve(i-1, nums)
#         return max(toPick, notToPick)


#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         return max(self.solve(n-2, nums[1:]), self.solve(n-2, nums[:-1]))

# Recursive + Memoization - O(n), O(n) + O(n)
#     def solve(self, i: int, nums: List[int], dp: List[int]) -> int:
#         if i < 0:
#             return 0
#         if dp[i] != -1:
#             return dp[i]
#         toPick = self.solve(i-2, nums, dp) + nums[i]
#         notToPick = self.solve(i-1, nums, dp)
#         dp[i] = max(toPick, notToPick)
#         return dp[i]


#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         fNums = []
#         lNums = []
#         for i in range(len(nums)):
#             if i != 0: fNums.append(nums[i])
#             if i != n-1: lNums.append(nums[i])
#         dp = [-1] * (n-1)
#         return max(self.solve(n-2, fNums, dp[:]), self.solve(n-2, lNums, dp))

# Iterative + Memoization(Bottom Up) - O(n), O(n)
#     def solve(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [-1] * n
#         dp[0] = nums[0]
#         for i in range(1, n):
#             toRob = nums[i]
#             if i>1: toRob += dp[i-2]
#             notToRob = dp[i-1]
#             dp[i] = max(toRob, notToRob)
#         return dp[n-1]
        
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1: return nums[0]
#         fNums = []
#         lNums = []
#         for i in range(n):
#             if i != 0: fNums.append(nums[i])
#             if i != n-1: lNums.append(nums[i])
#         return max(self.solve(fNums), self.solve(lNums))

# Iterative - O(n), O(1)
    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        prev2 = 0
        prev = nums[0]
        for i in range(1, n):
            toRob = nums[i]
            if i>1: toRob += prev2
            notToRob = prev
            curr = max(toRob, notToRob)
            prev2, prev = prev, curr
        return prev
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        fNums = []
        lNums = []
        for i in range(n):
            if i != 0: fNums.append(nums[i])
            if i != n-1: lNums.append(nums[i])
        return max(self.solve(fNums), self.solve(lNums))

ans = Solution().rob([1])
print(ans)