from random import seed
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Hashmap/Sets - O(n), O(n)
        # seen = set()
        # ans = []
        # for num in nums:
        #     if num in seen:
        #         ans.append(num)
        #     else:
        #         seen.add(num)
        # return ans

        # Array Manipulation
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            nums[abs(num) - 1] *= -1
        print(nums)
        
        return ans


ans = Solution().findDuplicates([4,3,2,7,8,2,3,1])
print(ans)