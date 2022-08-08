# https://www.youtube.com/watch?v=onLoX6Nhvmg&ab_channel=takeUforward
# https://leetcode.com/problems/3sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Two Pointers - O(n2),O(n)
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i==0 or nums[i] != nums[i-1]:
                left, right = i+1, len(nums)-1
                while left < right:
                    summ = nums[i] + nums[left] + nums[right]
                    if summ == 0:
                        ans.append((nums[i], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif summ < 0:  left += 1
                    else:   right -= 1
        return ans

ans = Solution().threeSum([0,0,0,0])
print(ans)