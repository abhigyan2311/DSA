from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target: return mid
            
            if nums[lo] <= nums[mid]:
                # Left to Mid is sorted
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                # Mid to Right is sorted
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
        return -1



ans = Solution().search([4,5,6,7,0,1,2], 0)
print(ans)