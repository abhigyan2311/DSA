from math import inf
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute Force - O(N^3)
        # maxProd = -inf
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)+1):
        #         prod = 1
        #         for k in range(i, j):
        #             prod *= nums[k]
        #         maxProd = max(prod, maxProd)
        # return maxProd
        
        # Optimized Brute Force - O(N^2)
        # maxProd = -inf
        # for i in range(len(nums)):
        #     prod = nums[i]
        #     for j in range(i+1, len(nums)):
        #         maxProd = max(prod, maxProd)
        #         prod *= nums[j]
        #     maxProd = max(prod, maxProd)
        # return maxProd

        # Optimized
        res = max(nums)
        currMin, currMax = 1, 1
        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
            else:
                tmp = currMax
                currMax = max(currMax*num, currMin*num, num)
                currMin = min(currMin*num, tmp*num, num)
                res = max(res, currMax)
        return res

ans = Solution().maxProduct([2,3,-2,4])
print(ans)