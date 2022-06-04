class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def isPossible(self, mid, A, B):
        allocatedStudents = 1
        totalPages = 0
        for i in range(len(A)):
            if A[i] > mid: return False
            if totalPages+A[i] > mid:
                allocatedStudents += 1
                totalPages += A[i]
            else:
                totalPages += A[i]
        if allocatedStudents > B: return False
        return True

    def books(self, A, B):
        lo, hi = min(A), sum(A)
        res = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if self.isPossible(mid, A, B):
                res = mid
                hi = mid-1
            else:
                lo = mid+1
        return res

ans = Solution().books([12, 34, 67, 90], 2)
print(ans)
        