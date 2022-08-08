from bisect import bisect_left
from typing import List

class Solution:
    # Recursive - O(2^N), O(N)
    # def buildSubsequence(self, ind: int, prevInd: int, nums: List[int]):
    #     # Base Case
    #     if ind == len(nums): return 0 
    #     # Not Pick
    #     notPickLen = 0 + self.buildSubsequence(ind+1, prevInd, nums)
    #     # Pick
    #     pickLen = 0
    #     if prevInd == -1 or nums[prevInd] < nums[ind]:
    #         pickLen = 1 + self.buildSubsequence(ind+1, ind, nums)
    #     return max(notPickLen, pickLen)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     return self.buildSubsequence(0, -1, nums)
    
    # Memoization - O(N^2), O(N^N) + O(N)
    # def buildSubsequence(self, ind: int, prevInd: int, nums: List[int], dp: List[List[int]]):
    #     # Base Case
    #     if ind == len(nums): return 0
    #     if dp[ind][prevInd+1] != -1: return dp[ind][prevInd+1]
    #     # Not Pick
    #     notPickLen = 0 + self.buildSubsequence(ind+1, prevInd, nums, dp)
    #     # Pick
    #     pickLen = 0
    #     if prevInd == -1 or nums[prevInd] < nums[ind]:
    #         pickLen = 1 + self.buildSubsequence(ind+1, ind, nums, dp)
    #     maxLen = max(notPickLen, pickLen)
    #     dp[ind][prevInd+1] = maxLen
    #     return maxLen

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [[-1]*n for _ in range(n+1)]
    #     return self.buildSubsequence(0, -1, nums, dp)
    
    # Tabulation - O(N^2), O(N^2)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [[0]*(n+1) for _ in range(n+1)]
    #     dp[n][n+1] = 0
    #     for ind in range(n-1, -1, -1):
    #         for prevInd in range(ind-1, -2, -1):
    #             # Not Pick
    #             notPickLen = 0 + dp[ind+1][prevInd+1]
    #             # Pick
    #             pickLen = 0
    #             if prevInd == -1 or nums[prevInd] < nums[ind]:
    #                 pickLen = 1 + dp[ind+1][ind+1]
    #             maxLen = max(notPickLen, pickLen)
    #             dp[ind][prevInd+1] = maxLen 
    #     return dp[0][0]

    # Tabulation + Space Optimization - O(N^2), O(2N)
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     curr = [0] * (n+1)
    #     next = [0] * (n+1)
    #     for ind in range(n-1, -1, -1):
    #         for prevInd in range(ind-1, -2, -1):
    #             # Not Pick
    #             notPickLen = 0 + next[prevInd+1]
    #             # Pick
    #             pickLen = 0
    #             if prevInd == -1 or nums[prevInd] < nums[ind]:
    #                 pickLen = 1 + next[ind+1]
    #             maxLen = max(notPickLen, pickLen)
    #             curr[prevInd+1] = maxLen
    #         next = curr
    #     return curr[0]

    # Tabulation 2
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1]*n
    #     maxi = 1
    #     backtrackArr = [0]*n
    #     lastInd = 0
    #     for i in range(1, n):
    #         backtrackArr[i] = i
    #         for j in range(0, i):
    #             if nums[j] < nums[i] and 1+dp[j] > dp[i]:
    #                 dp[i] = 1+dp[j]
    #                 backtrackArr[i] = j
    #         if dp[i] > maxi:
    #             maxi = dp[i]
    #             lastInd = i

    #     lis = [nums[lastInd]]
    #     while backtrackArr[lastInd] != lastInd:
    #         lastInd = backtrackArr[lastInd]
    #         lis.append(nums[lastInd])
    #     lis.reverse()
    #     return maxi, lis

    # Binary Search
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        temp = []
        temp.append(nums[0])
        for i in range(1, n):
            if nums[i] > temp[-1]: temp.append(nums[i])
            else:
                indToReplace = bisect_left(temp, nums[i])
                temp[indToReplace] = nums[i]
        return len(temp)
    
    def binSearch(self, temp: List[int], target: int):
        left, right = 0, len(temp)
        while left < right:
            mid = (left+right)//2
            if temp[mid] == target: return mid
            elif temp[mid] < target:
                left += 1
            else:
                if target > temp[mid-1]: return mid
                right -= 1


ans = Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
print(ans)