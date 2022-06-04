from math import ceil, inf

class Solution:
	# @param A : list of list of integers
	# @return an integer
    def countEl(self, A, target):
        totalCount = 0
        for i in range(len(A)):
            lo, hi = 0, len(A[i])-1
            while lo<=hi:
                mid = (lo+hi)//2
                if A[i][mid] <= target:
                    lo = mid+1
                else: hi = mid-1
            totalCount += lo
        return totalCount

    def findMedian(self, A):
        n, m = len(A), len(A[0])
        size = n*m

        lo, hi = 1, 1e9
        while lo<=hi:
            mid = int((lo+hi)//2)
            countLen = self.countEl(A, mid)
            if countLen <= size//2:
                lo = mid+1
            else: hi = mid-1
        return lo

ans = Solution().findMedian(
        [   [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]   
        ]
    )
print(ans)

# 1 2 3 3 5 6 6 9 9

