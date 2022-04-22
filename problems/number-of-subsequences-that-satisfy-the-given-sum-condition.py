# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
# https://youtu.be/eQCS_v3bw0Q

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Recursion - O(2^n), O(n) -- TLE
        # def myRecSum(i: int, arr: List[int]):
        #     if i == n:
        #         if len(arr) > 0 and min(arr)+max(arr) <= target:
        #             return 1
        #         else:
        #             return 0
        #     arr.append(nums[i])
        #     left = myRecSum(i+1, arr)
        #     arr.pop()
        #     right = myRecSum(i+1, arr)
        #     return left+right

        # n = len(nums)
        # ans = myRecSum(0, [])
        # return ans

        # Two Pointer - O(nlogn), O(1)
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r-l, mod)
                l += 1
        return res % mod

ans = Solution().numSubseq([3,5,6,7], 9)
print(ans)

