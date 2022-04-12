# https://www.youtube.com/watch?v=1uu3g_uu8O0&ab_channel=Pepcoding
# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[left] <= nums[mid]):
                # Left to Mid is Sorted
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif (nums[mid] <= nums[right]):
                # Mid to Right is Sorted
                if (target > nums[mid] and target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


answer = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
print(answer)
