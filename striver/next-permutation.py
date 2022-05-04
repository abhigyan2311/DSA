from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2 
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1    
            nums[i], nums[j] = nums[j], nums[i]
        self.reverseArr(nums, i+1, n)
        
        return nums

    def reverseArr(self, nums: List[int], start: int, end: int) -> None:
        end -= 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


ans = Solution().nextPermutation([1,1])
print(ans)