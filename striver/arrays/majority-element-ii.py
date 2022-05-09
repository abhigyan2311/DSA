from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Better - O(N), O(N)
        # hashmap = Counter(nums)
        # ans = []
        # target = len(nums)//3
        # for ind in hashmap:
        #     if hashmap[ind] > target:
        #         ans.append(ind)
        # return ans

        # Optimal - O(N), O(1)
        n = len(nums)
        num1 = num2 = -1
        c1 = c2 = 0
        for num in nums:
            if num == num1: c1 += 1
            elif num == num2: c2 += 1
            elif c1 == 0: 
                num1 = num
                c1 = 1
            elif c2 == 0: 
                num2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = c2 = 0
        for num in nums:
            if num == num1: c1 += 1
            elif num == num2: c2 += 1

        ans = []
        if c1 > n/3:
            ans.append(num1)
        if c2 > n/3:
            ans.append(num2)
        return ans



ans = Solution().majorityElement([1,1,1,2,3,7,8,1,6,9])
print(ans)
        