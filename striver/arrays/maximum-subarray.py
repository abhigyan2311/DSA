from math import inf
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxi = -inf
        for num in nums:
            summ += num
            maxi = max(maxi, summ)
            if summ < 0: summ = 0
        return maxi

ans = Solution().maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3])
print(ans)
        