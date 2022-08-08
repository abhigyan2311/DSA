from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestStreak = 0
        hm = set(nums)
        for num in nums:
            if num-1 not in hm:
                currenStreak = 1
                currentNum = num+1
                while currentNum in hm:
                    currenStreak += 1
                    currentNum += 1
                longestStreak = max(longestStreak, currenStreak)
        return longestStreak
        
ans = Solution().longestConsecutive([100,4,200,1,3,2])
print(ans)
        