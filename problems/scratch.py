from typing import List

def findSqrt(x: int) -> int:
    if x < 2:
        return x
    lo, hi = 2, x//2
    while lo <= hi:
        mid = (lo + hi)//2
        midPow = mid*mid
        if midPow == x:
            return mid
        elif midPow < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi



a = findSqrt(8)
print(a)

