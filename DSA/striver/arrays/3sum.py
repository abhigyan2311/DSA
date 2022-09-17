# https://www.youtube.com/watch?v=onLoX6Nhvmg&ab_channel=takeUforward
# https://leetcode.com/problems/3sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Two Pointers - O(2NlogN), O(1)
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                left, right = i+1, len(nums)-1
                while left < right:
                    summ = nums[i] + nums[left] + nums[right]
                    if summ == 0:
                        ans.append((nums[i], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif summ < 0:
                        left += 1
                    else:
                        right -= 1
        return ans

        # Approach 2: Hashset - O(n2),O(n)
        # nums.sort()
        # ans = []
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         break
        #     if i == 0 or nums[i-1] != nums[i]:
        #         seen = set()
        #         j = i + 1
        #         while j < len(nums):
        #             complement = -nums[i] - nums[j]
        #             if complement in seen:
        #                 ans.append([nums[i], nums[j], complement])
        #                 while j+1 < len(nums) and nums[j] == nums[j+1]:
        #                     j += 1
        #             seen.add(nums[j])
        #             j += 1
        # return ans

        # Approach 3: Hashset without sorting - O(n2),O(n)
        # ans, dups = set(), set()
        # seen = {}
        # for i in range(len(nums)):
        #     if nums[i] not in dups:
        #         dups.add(nums[i])
        #         for j in range(i+1, len(nums)):
        #             complement = -(nums[i] + nums[j])
        #             if complement in seen and seen[complement] == i:
        #                 ans.add(tuple(sorted((nums[i], nums[j], complement))))
        #             seen[nums[j]] = i
        # return ans


ans = Solution().threeSum([0, 0, 0, 0])
print(ans)
