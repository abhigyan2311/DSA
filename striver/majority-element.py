from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        el = -1
        for i in range(len(nums)):
            if counter == 0:
                el = nums[i]
            if nums[i] == el:
                counter += 1
            else:
                counter -= 1
        return el

ans = Solution().majorityElement([2,2,1,1,1,2,2])
print(ans)