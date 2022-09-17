from math import ceil, inf
from typing import List


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def countEls(self, A: List[List[int]], target: int) -> int:
        totalCount = 0
        m, n = len(A), len(A[0])
        for i in range(m):
            lo, hi = 0, n-1
            while lo <= hi:
                mid = (lo+hi)//2
                if A[i][mid] <= target:
                    lo = mid+1
                else:
                    hi = mid-1
            totalCount += lo
        return totalCount

    def findMedian(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        size = m*n
        lo, hi = 0, 1e9
        while lo <= hi:
            mid = (lo+hi)//2
            countLen = self.countEls(A, mid)
            if countLen <= size//2:
                lo = mid+1
            else:
                hi = mid-1
        return lo

    # Search space is 10**9 which is equivalent to 2**32. So TC = O(log2(2**32) * N * logM) => O(32*NlogM)


ans = Solution().findMedian(
    [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]
     ]
)
print(ans)

# 1 2 3 3 5 6 6 9 9
