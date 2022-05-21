from re import L
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute Force - O(N^2), O(1)
        # n = len(height)
        # totalWater = 0
        # for i in range(n):
        #     leftMax, rightMax = 0, 0
        #     # Compute leftMax
        #     for l in range(0, i):
        #         leftMax = max(leftMax, height[l])
            
        #     # Compute rightMax
        #     for r in range(i+1, n):
        #         rightMax = max(rightMax, height[r])
            
        #     # Compute current height
        #     currentWater = min(leftMax, rightMax) - height[i]
        #     if currentWater > 0: totalWater += currentWater
        # return totalWater

        # Better - O(3N), O(2N)
        n = len(height)
        totalWater = 0
        preMax, sufMax = [-1] * n, [-1] * n

        # Compute max prefix array
        preMax[0] = height[0]
        for i in range(1, n):
            preMax[i] = max(preMax[i-1], height[i])
        
        # Compute max prefix array
        sufMax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            sufMax[i] = max(sufMax[i+1], height[i])

        # Compute current column water height
        for i in range(n):
            totalWater += min(preMax[i], sufMax[i]) - height[i]
        return totalWater

        # Optimal - O(N), O(1)
        # n = len(height)
        # left, right = 0, n-1
        # leftMax, rightMax = 0, 0
        # totalWater = 0
        # while left <= right:
        #     if height[left]<=height[right]:
        #         if height[left]>=leftMax:   leftMax = height[left]
        #         else:   totalWater += leftMax - height[left]
        #         left += 1
        #     else:
        #         if height[right]>=rightMax: rightMax = height[right]
        #         else:   totalWater += rightMax - height[right]
        #         right -= 1
        # return totalWater
ans = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(ans)
        