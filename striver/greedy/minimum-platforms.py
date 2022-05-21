from math import inf
from typing import List


class Solution:    
    def minimumPlatform(self, n: int, arr: List[int], dep: List[int]):
        arr.sort()
        dep.sort()

        platforms = 1
        maxPlatforms = 1
        i, j = 1, 0
        while i < n-1:
            nextArr = arr[i]
            preDep = dep[j]
            if nextArr <= preDep:
                i += 1
                platforms += 1
            else:
                platforms -= 1
                j += 1
            maxPlatforms = max(maxPlatforms, platforms)

        return maxPlatforms

ans = Solution().minimumPlatform(6, [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000])
print(ans)