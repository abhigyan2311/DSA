from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums)):
            ans = ans ^ nums[i]
        for i in range(1, len(nums)):
            ans = ans ^ i
        return ans


answer = Solution().findDuplicate([3, 1, 3, 4, 2])
print(answer)
