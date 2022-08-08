from typing import List


class Solution:
    # Brute Force - O(2^n) + (2^n)*logn
    # def recPowerSet(self, i: int, arr: List[int], nums: List[int], ans: List[List[int]]):
    #         if i == len(nums):
    #             ans.append(sorted(arr[:]))
    #             return
    #         arr.append(nums[i]) 
    #         self.recPowerSet(i+1, arr, nums, ans)
    #         arr.pop()
    #         self.recPowerSet(i+1, arr, nums, ans)
    
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #     self.recPowerSet(0, [], nums, ans)
    #     res = []
    #     for el in ans:
    #         if el not in res:
    #             res.append(el)
    #     return res

    # Best Approach - O(2^n * n), O(2^n) * O(k) 
    def recSubSets(self, ind: int, ds: List[int], nums: List[int], ans: List[List[int]]):
        ans.append(ds[:])
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i-1]: continue
            ds.append(nums[i])
            self.recSubSets(i+1, ds, nums, ans)
            ds.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ds, ans = [], []
        self.recSubSets(0, ds, nums, ans)
        return ans

ans = Solution().subsetsWithDup([1,2,2])
print(ans)