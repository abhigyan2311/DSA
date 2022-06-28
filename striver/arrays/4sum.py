from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int, start: int):
        left = start
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Approach 1: 3 Pointer + Binary Search
        # ans = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             threeSum = nums[i]+nums[j]+nums[k]
        #             comp = target - threeSum
        #             foundNumInd = self.binarySearch(nums, comp, k+1)
        #             if foundNumInd:
        #                 ans.add((nums[i], nums[j], nums[k], nums[foundNumInd]))
        # return ans

        ans = []
        nums.sort()
        n = len(nums)
        i = 0
        while i<n:
            j = i+1
            while j<n:
                left, right = j+1, n-1
                twoSum = nums[i] + nums[j]
                while left<right:
                    nextTwoSum = nums[left] + nums[right]
                    targetSum = target - twoSum
                    if nextTwoSum < targetSum:
                        left += 1
                    elif nextTwoSum > targetSum:
                        right -= 1
                    else:
                        q3, q4 = nums[left], nums[right]
                        ans.append([nums[i], nums[j], q3, q4])
                        while left < right and nums[left] == q3:
                            left += 1
                        while left < right and nums[right] == q4:
                            right -= 1
                while j+1 < n and nums[j] == nums[j+1]:
                    j += 1
                j+=1
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            i+=1
        return ans

        # Approach 2: 2 Pointer
        ans = []
        nums.sort()
        n = len(nums)
        i  = 0
        while i<n:
            j = i+1
            while j<n:
                left, right = j+1, n-1
                while left < right:
                    twoSum = nums[i] + nums[j]
                    nextTwoSum = nums[left] + nums[right]
                    targetSum = target - twoSum
                    if nextTwoSum < targetSum:
                        left += 1
                    elif nextTwoSum > targetSum:
                        right -= 1
                    else:
                        q3, q4 = nums[left], nums[right]
                        ans.append([nums[i], nums[j], q3, q4])
                        while left < right and nums[left] == q3:
                            left += 1
                        while left < right and nums[right] == q4:
                            right -= 1
                while j+1 < n and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return ans

ans = Solution().fourSum([-2,-1,-1,1,1,2,2], 0)
print(ans)
        