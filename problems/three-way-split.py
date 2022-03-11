from typing import *

def threeWaySplit(arr: List[int]) -> int:
    left, right = 1, len(arr) - 1
    ans = 0
    while left <= right:
        s1 = sum(arr[:left])
        s3 = sum(arr[right:])
        if s1 < s3:
            left += 1
        elif s1 > s3:
            right -= 1
        else:
            ans = s1
            left += 1
            right -= 1
    return ans

exInput = "3 3"
arrExInput = exInput.split()
map_object = map(int, arrExInput)
list_of_integers = list(map_object)

ans = threeWaySplit(list_of_integers)
print(ans)