from re import I
from typing import List


class Solution:
    def maxLen(self, arr: List[int]):
        hm = {}
        maxi = 0
        summ = 0
        for ind in range(len(arr)):
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

ans = Solution().maxLen([15,-2,2,-8,1,7,10,23])
print(ans)