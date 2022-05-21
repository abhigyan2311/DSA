from cmath import inf
from collections import Counter
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        maxCarpetLen = -inf
        tiles.sort()
        #Merge tiles
        i = 0
        while i <= len(tiles) - 1:
            curr = tiles[i]
            nexttLen = -inf
            if i == len(tiles) - 1:
                maxCarpetLen = max(maxCarpetLen, curr[1] - curr[0] + 1)
            else:
                nextt = tiles[i+1]
                nexttLen = nextt[1] - nextt[0] + 1
                if curr[1] + 1 == nextt[0]:
                    curr = [curr[0], nextt[1]]
                    tiles[i] = curr
                    tiles.pop(i+1)
                    i -= 1
                currLen = curr[1] - curr[0] + 1
                maxCarpetLen = max(maxCarpetLen, currLen, nexttLen)
            i += 1
        return maxCarpetLen
    
    def largestVariance(self, s: str) -> int:
        maxV = 0
        # Calculate all substrs
        substrs = [s[i: j] for i in range(len(s))
          for j in range(i + 1, len(s) + 1)]

        for el in substrs:
            cm = Counter(el)
            highestEl = cm.most_common()[0][1]
            lowestEl = inf
            for i in cm:
                lowestEl = min(lowestEl, cm[i])
            maxV = max(maxV, highestEl - lowestEl)
        return maxV

# ans = Solution().maximumWhiteTiles([[8051,8057],[8074,8089],[7994,7995],[7969,7987],[8013,8020],[8123,8139],[7930,7950],[8096,8104],[7917,7925],[8027,8035],[8003,8011]], 9854)
ans = Solution().largestVariance('abcde')
print(ans)