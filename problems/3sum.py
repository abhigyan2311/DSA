from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Two Pointers - O(n2),O(n)
        # nums.sort()
        # ans = []
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         break
        #     if i == 0 or nums[i-1] != nums[i]:
        #         left, right = i+1, len(nums) - 1
        #         while left < right:
        #             sum = nums[i] + nums[left] + nums[right]
        #             if sum == 0:
        #                 ans.append([nums[i], nums[left], nums[right]])
        #                 left += 1
        #                 right -= 1
        #                 while left < right and nums[left] == nums[left - 1]:
        #                     left += 1
        #             elif sum < 0:
        #                 left += 1
        #             else:
        #                 right -= 1
        # return ans

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
        ans, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        ans.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return ans

ans = Solution().threeSum([-1,0,1,2,-1,-4])
print(ans)