class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Clean array
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        
        # Mark positive nums
        for i in range(n):
            val = abs(nums[i])
            if val <= n:
                nums[val-1] = -abs(nums[val-1])
        
        # Find minimum positive
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1  