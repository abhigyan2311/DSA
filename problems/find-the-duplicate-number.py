# https://leetcode.com/problems/find-the-duplicate-number/
# https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode
# https://www.youtube.com/watch?v=32Ll35mhWg0&ab_channel=takeUforward
# https://youtu.be/oVa8DfUDKTw


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
