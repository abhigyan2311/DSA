from typing import Counter, List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestStreak = 0
        hm = Counter(nums)
        for num in nums:
            if num-1 not in hm:
                currNum = num+1
                currStreak = 1
                while currNum in hm:
                    currStreak += 1
                    currNum += 1
                longestStreak = max(longestStreak, currStreak)
        return longestStreak
        

ans = Solution().longestConsecutive([100,4,200,1,3,2])
print(ans)
        