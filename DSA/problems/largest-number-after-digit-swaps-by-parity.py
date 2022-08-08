# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity

class Solution:
    def largestInteger(self, num: int) -> int:
        # Brute Force
        # nums = [int(x) for x in str(num)]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         # Even
        #         if nums[i]%2 == 0 and nums[j]%2 == 0 and nums[i] < nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         # Odd
        #         if nums[i]%2 != 0 and nums[j]%2 != 0 and nums[i] < nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        # return int("".join(map(str, nums)))
    
        # Approach 2
        nums = [int(x) for x in str(num)]
        odd, even = [],[]
        for a in nums:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        even.sort()
        odd.sort()
        res = 0
        for a in nums:
            if a % 2 == 0:
                res = res*10 + even.pop()
            else:
                res = res*10 + odd.pop()
        return res

ans = Solution().largestInteger(65875)
print(ans)