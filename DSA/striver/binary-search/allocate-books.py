class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        res = -1
        if B > len(A):
            return -1

        # Is the array sorted?
        lo, hi = min(A), sum(A)
        res = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if self.isAllocationPossible(mid, A, B):
                hi = mid-1
                res = mid
            else:
                lo = mid+1
        return res

    def isAllocationPossible(self, target, A, totalStudents):
        allocatedStudents = 1
        currentPages = 0
        for pages in A:
            if pages > target:
                return False
            if currentPages + pages > target:
                allocatedStudents += 1
                currentPages = pages
            else:
                currentPages += pages
        if allocatedStudents > totalStudents:
            return False
        return True


ans = Solution().books([12, 34, 67, 90], 2)
print(ans)
