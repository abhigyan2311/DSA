from typing import *

def appleAndCoupon(m : int, arr: List[int])-> int:
    sortedArr = sorted(arr)  # - O(nLogn)
    selectedApples = sortedArr[-m:]
    freeApple = selectedApples[0]
    arr.remove(freeApple)  # - O(n)
    # print(arr)
    return sum(arr)

ans = appleAndCoupon(3, [5, 2, 4, 1, 3])
print(ans)