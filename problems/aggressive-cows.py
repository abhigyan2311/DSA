# https://www.youtube.com/watch?v=wSOfYesTBRk
# https://youtu.be/YTTdLgyqOLY

from typing import List

def isPossible(stalls: List[int], aggCow: int, mid: int) -> bool:
    currentCowPos = stalls[0]
    totalCows = 1
    for stall in stalls:
        if (stall - currentCowPos >= mid):
            totalCows += 1
            if totalCows == aggCow: 
                return True
            currentCowPos = stall
    return False

def allocateCows(stalls: List[int], aggCow: int) -> int:
    stalls.sort()
    lo, hi = 1, max(stalls) - min(stalls)
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if isPossible(stalls, aggCow, mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

ans = allocateCows([4, 2, 1, 3, 6], 2)
print(ans)