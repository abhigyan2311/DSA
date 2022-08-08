from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Better - O(n) + O(nlogn), O(1)
        # Find the correct row
        # rowInd = -1
        # for row in range(len(matrix)):
        #     if matrix[row][0] > target: break
        #     rowInd = row
        
        # # Binary search in row
        # left, right = 0, len(matrix[0]) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     pickedRow = matrix[rowInd]
        #     if pickedRow[mid] == target:
        #         return True
        #     elif target > pickedRow[mid]:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return False

        # Optimal -  O(nlogn), O(1)
        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows*cols-1
        while left <= right:
            mid = (left+right)//2
            pickedEl = matrix[mid//cols][mid%cols]
            if pickedEl == target:
                return True
            elif pickedEl > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

        
ans = Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 23)
print(ans)