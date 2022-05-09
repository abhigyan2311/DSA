from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hm:
                return [hm[comp], i]
            hm[nums[i]] = i
        return []

ans = Solution().twoSum([2,7,11,15], 9)
print(ans)