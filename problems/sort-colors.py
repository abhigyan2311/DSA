from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # c0,c1,c2 = 0,0,0
        # for num in nums:
        #     if num == 0:
        #         c0 += 1
        #     elif num == 1:
        #         c1 += 1
        #     else:
        #         c2 += 1
        # nums[:c0] = [0] * c0
        # nums[c0:c0+c1] = [1] * c1
        # nums[c0+c1:] = [2] * c2
        # print(nums)

        # Approach 2: Dutch Flag Algorithm
        lo,mid,hi = 0,0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                mid += 1
                lo += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[hi], nums[mid] = nums[mid], nums[hi]
                hi -= 1
        print(nums)


Solution().sortColors([0,1,0,1,1,2,1,2,0])        