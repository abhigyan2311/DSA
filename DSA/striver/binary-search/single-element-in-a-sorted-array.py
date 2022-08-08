from typing import List


class Solution:
        # XOR - O(N), O(1)
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    #     ans = 0
    #     for num in nums:
    #         ans ^= num
    #     return ans
        
        # Binary Search - O(logN), O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 2
        while lo <= hi:
            mid = (lo+hi)//2
            if mid%2 != 0:
                if nums[mid] == nums[mid-1]:
                    lo = mid+1
                else:
                    hi = mid-1
            else:
                if nums[mid] == nums[mid+1]:
                    lo = mid+1
                else:
                    hi = mid-1
        return lo

ans = Solution().singleNonDuplicate([3,3,7,7,10,11,11])
print(ans)