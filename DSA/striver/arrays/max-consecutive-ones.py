from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        
        maxLen = 0
        i = 0
        while i < n-1:
            j = i+1
            while j < n and nums[i] == nums[j]:
                j += 1
            maxLen = max(maxLen, j-i)
            i += 1
        return maxLen

ans = Solution().findMaxConsecutiveOnes([1,0,1,1,0,1])
print(ans)