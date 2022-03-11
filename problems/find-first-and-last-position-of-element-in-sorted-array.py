from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Linear Scan
        # left, right = -1, -1
        # if (len(nums) == 1 and target == nums[0]):
        #     return [0,0]
        # for i in range(len(nums)):
        #     print(f"i:{i} and num:{nums[i]}")
        #     if (nums[i] == target) and (left == -1):
        #         left = i
        #         print(f"left: {left}")
        #     if(len(nums) - 1 != i and left != -1 and nums[i] == target):
        #         right = i
        #     if (len(nums) - 1 == i and nums[i] == target):
        #         right = i
        #         break
        # return [left, right]


        # Binary Search
        def findLeftMostIndex():
            left, right = 0, len(nums)-1
            leftMostIndex = -1
            while left <= right:
                mid = (left+right)//2
                if target == nums[mid]:
                    leftMostIndex = mid
                    right = mid - 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return leftMostIndex
        
        def findRightMostIndex(leftIndex: int):
            left, right = leftIndex, len(nums)-1
            rightMostIndex = -1
            while left <= right:
                mid = (left+right)//2
                if target == nums[mid]:
                    rightMostIndex = mid
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return rightMostIndex

        left = findLeftMostIndex()
        if (left == -1):
            return [-1,-1]
        right = findRightMostIndex(left)
        return [left, right]

answer = Solution().searchRange([1,2,3], 1)
print(answer)