def findNthRootOfM(n,m):
    lo, hi = 1, m
    eps = 1e-6
    while (hi-lo) > eps:
        mid = (lo+hi)/2.0
        if mid**n < m:
            lo = mid
        else:
            hi = mid
    return mid

    low, high = 1, m
    eps = 0.00000001
    mid = (low + high) / 2
    while abs(mid ** n - m) >= eps:
        if mid ** n > m:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2
    return round(mid,6)

print(findNthRootOfM(3, 27))