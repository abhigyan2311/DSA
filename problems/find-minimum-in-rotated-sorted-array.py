from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]

        left = 0
        right = len(nums) - 1
        if (nums[left] < nums[right]):
            return nums[left]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return nums[left]

answer = Solution().findMin([4, 5, 6, 7, 0, 1, 2])
print(answer)