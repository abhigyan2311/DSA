from typing import List


class Solution:
    def merge(self, nums: List[int], left: int, mid: int, right: int) -> int:
        counter = 0

        leftArr = nums[left:mid+1]
        rightArr = nums[mid+1:right+1]

        j = 0
        for i in range(len(leftArr)):
            while j < len(rightArr) and leftArr[i] > 2*rightArr[j]:
                j += 1
            # If the above loop satisfies then for all next i the previous j will form the reverse pairs
            counter += j

        i, j = 0, 0
        k = left
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                nums[k] = leftArr[i]
                i+=1
            else:
                nums[k] = rightArr[j]
                j+=1
            k+=1
        
        while i<len(leftArr):
            nums[k] = leftArr[i]
            i+=1
            k+=1
        while j<len(rightArr):
            nums[k] = rightArr[j]
            j+=1
            k+=1
        
        return counter
    def mergeSort(self, nums, left: int, right: int) -> int:
        if left >= right: return 0
        counter = 0
        mid = (left+right) // 2
        counter += self.mergeSort(nums, left, mid)
        counter += self.mergeSort(nums, mid+1, right)
        counter += self.merge(nums, left, mid, right)
        return counter

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums)-1)

ans = Solution().reversePairs([2,4,3,5,1])
print(ans)