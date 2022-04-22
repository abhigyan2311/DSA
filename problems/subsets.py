# https://leetcode.com/problems/subsets/
# https://youtu.be/AxNNVECce8c

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Recursion - O(2^n), O(n)
        def recPowerSet(i: int, arr: List[int]):
            if i == n:
                ans.append(arr[:])
                return
            arr.append(nums[i]) 
            recPowerSet(i+1, arr)
            arr.pop()
            recPowerSet(i+1, arr)
        
        n = len(nums)
        ans = []
        recPowerSet(0, [])
        return ans


ans = Solution().subsets([3,1,2])
print(ans)