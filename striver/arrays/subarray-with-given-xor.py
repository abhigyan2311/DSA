from collections import defaultdict
from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A: List[int], B: int):
        visited = defaultdict(int)
        count, xorr = 0, 0
        for num in A:
            xorr ^= num
            if xorr == B:
                count += 1
            Y = xorr ^ B
            if Y in visited:
                count += visited[Y]
            # if xorr in visited:
            visited[xorr] += 1
            # else:
            #     visited[xorr] = 1
        return count

ans = Solution().solve([ 4, 2, 2, 6, 4 ], 6)
print(ans)