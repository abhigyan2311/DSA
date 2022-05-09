from typing import List


class Solution:
    def maxLen(self, n: int, arr: List[int]):
        hm = {}
        maxi = 0
        summ = 0
        for ind in range(n):
            summ += arr[ind]
            if summ == 0:
                maxi = ind+1
            else:
                if summ in hm:
                    prefixInd = hm[summ]
                    maxi = max(maxi, ind-prefixInd)
                else:
                    hm[summ] = ind
        return maxi

ans = Solution().maxLen(4, [-1, 1, 1, -1])
print(ans)