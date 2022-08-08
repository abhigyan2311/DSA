from typing import List, Dict

class Solution:
    # Approach 1 - O(n! * n), O(n) + O(n)
    # def recFindPerm(self, ds: List[int], hm: Dict[int, int], nums: List[int], ans: List[List[int]]):
    #     if len(ds) == len(nums):
    #         ans.append(ds[:])
    #         return
        
    #     for i in range(0, len(nums)):
    #         if nums[i] in hm:
    #             continue
    #         ds.append(nums[i])
    #         hm[nums[i]] = 1
    #         self.recFindPerm(ds, hm, nums, ans)
    #         ds.pop()
    #         del hm[nums[i]]
    
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #     hm = {}
    #     self.recFindPerm([], hm, nums, ans)    
    #     return ans

    # Approach 2 - O(n! * n), O(n)
    def recFindPerm(self, index: int, nums: List[int], ans: List[List[int]]):
        if index == len(nums):
            ans.append(nums[:])
            return
        
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.recFindPerm(index+1, nums, ans)
            nums[i], nums[index] = nums[index], nums[i]     

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.recFindPerm(0, nums, ans)    
        return ans

ans = Solution().permute([1,2,3])
print(ans)