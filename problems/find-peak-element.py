# https://leetcode.com/problems/find-peak-element/

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Approach 1: Linear Scan - O(n), O(1)
        # if len(nums) == 1:
        #     return 0
        # for i in range(len(nums)):
        #     if i < len(nums)-1 and nums[i] > nums[i+1]:
        #         return i
        # return len(nums) - 1
    
        # Approach 2: Binary Search - O(logn), O(1)
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left

        # Recursion
    #     return self.search(nums, 0, len(nums) - 1)

    # def search(self, nums: List[int], left: int, right: int) -> int:
    #     if left == right:
    #         return left
    #     mid = (left + right) // 2
    #     if nums[mid] > nums[mid + 1]:
    #         return self.search(nums, left, mid)
    #     else:
    #         return self.search(nums, mid + 1, right)

answer = Solution().findPeakElement([1, 2, 3, 1])
print(answer)
