from cmath import inf
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lse, rse = [None]*n, [None]*n
        
        # Compute LSE
        st = []
        for i in range(n):
            while st and st[-1][1] >= heights[i]:
                st.pop()
            if not st: lse[i] = 0
            else: lse[i] = st[-1][0] + 1
            st.append((i, heights[i]))
            
        # Compute RSE
        st = []
        for i in range(n-1, -1, -1):
            while st and heights[i] <= st[-1][1]:
                st.pop()
            if not st:
                rse[i] = n-1
            else:
                rse[i] = st[-1][0] - 1
            st.append((i, heights[i]))

        maxArea = -inf
        for i in range(n):
            area = (rse[i] - lse[i] + 1)*heights[i]
            maxArea = max(maxArea, area)
        return maxArea

ans = Solution().largestRectangleArea([2,1,5,6,2,3,1])
print(ans)