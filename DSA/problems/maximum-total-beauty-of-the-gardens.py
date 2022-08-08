# https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

from typing import List

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort(reverse=True)
        completeNum = 0
        sumToRight = flowers[:] + [0]
        for i in range(len(sumToRight)-2, -1, -1):
            sumToRight[i] += sumToRight[i+1]
        
        while completeNum < len(flowers) and flowers[completeNum] >= target:
            completeNum += 1
        
        return 0


ans = Solution().maximumBeauty([1,3,1,1], 7, 6, 12, 1)