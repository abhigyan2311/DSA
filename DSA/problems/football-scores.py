from typing import List
from bisect import *

def counts(teamA: List[int], teamB: List[int]) -> List[int]:
    ans = []
    teamA.sort()
    for scoreB in teamB:
        # idx = bisect_right(teamA, scoreB)
        # ans.append(idx)
        if teamA[-1] <= scoreB:
            ans.append(len(teamA))
        else:
            left, right = 0, len(teamA) - 1
            while left < right:
                mid = (left+right)//2
                if teamA[mid] <= scoreB:
                    left = mid + 1
                else:
                    right = mid
            ans.append(right)
    return ans

ans = counts([3,3,4,5,4], [2,4])
print(ans)


