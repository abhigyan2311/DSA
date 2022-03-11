from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Iteration
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     pivot = (left + right) // 2
        #     if nums[pivot] > nums[pivot + 1]:
        #         right = pivot
        #     else:
        #         left = pivot + 1
        # return left

        # Recursion
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return left
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, left, mid)
        else:
            return self.search(nums, mid + 1, right)

answer = Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
print(answer)
