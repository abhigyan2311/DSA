class Solution:
    # Brute Force - O(N^2), O(1)
    # def canPlace(self, dist, stalls, cows):
    #     lastCow = stalls[0]
    #     count = 1
    #     for i in range(len(stalls)):
    #         if stalls[i]-lastCow >= dist:
    #             lastCow = stalls[i]
    #             count += 1
    #     if count == cows: return True
    #     return False

    # def aggCows(self, stalls, cows):
    #     stalls.sort()
    #     maxD = stalls[-1]-stalls[0]
    #     res = -1
    #     for dist in range(1, maxD+1):
    #         if self.canPlace(dist, stalls, cows):
    #             res = max(res, dist)
    #     return res

    # Optimal - O(NLogN), O(1)
    def canPlace(self, dist, stalls, cows):
        lastCow = stalls[0]
        count = 1
        for i in range(len(stalls)):
            if stalls[i] - lastCow >= dist:
                lastCow = stalls[i]
                count += 1
        if count >= cows: return True
        return False
            

    def aggCows(self, stalls, cows):
        stalls.sort()
        lo, hi = 1, stalls[-1]-stalls[0]
        res = -1
        while lo<=hi:
            mid = (lo+hi)//2
            if self.canPlace(mid, stalls, cows):
                lo = mid+1
                res = mid
            else:
                hi=mid-1
        return res

ans = Solution().aggCows([1, 2, 8, 4, 9], 3)
print(ans)
            