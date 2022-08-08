# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
        if nums[len(nums) - 1] > nums[0]:
            count += 1
        return count <= 1


ans = Solution().check([3,4,5,1,2,1])
print(ans)