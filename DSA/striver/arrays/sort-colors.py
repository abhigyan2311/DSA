from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Approach 1: Count and Sort
        # c0, c1, c2 = 0,0,0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         c0 += 1
        #     elif nums[i] == 1:
        #         c1 += 1
        #     else:
        #         c2 += 1
        # nums[:c0] = [0] * c0
        # nums[c0:c0+c1] = [1] * c1
        # nums[c0+c1:] = [2] * c2

        low, mid = 0, 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums


ans = Solution().sortColors([2, 1, 0, 0, 1, 2, 0, 1, 2, 0, 1, 1, 2, 2, 0])
print(ans)
