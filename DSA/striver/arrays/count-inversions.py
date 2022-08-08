from typing import List

# Brute Force - O(N^2), O(1)
# def getInversions(arr, n):
#     counter = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] > arr[j]:
#                 counter += 1
#     return counter

# Merge Sort - O(NlogN), O(N)
def merge(arr: List[int], left: int, mid: int, right: int) -> int:
    invCount = 0
    leftArr = arr[left: mid+1]
    rightArr = arr[mid+1:right+1]
    i, j = 0, 0
    k = left
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
            invCount += len(leftArr[i:])
        k += 1
    
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1
    
    return invCount

def mergeSort(arr: List[int], left: int, right: int) -> int:
    if left >= right: return 0
    invCount = 0
    mid = (left+right)//2
    invCount += mergeSort(arr, left, mid)
    invCount += mergeSort(arr, mid+1, right)
    invCount += merge(arr, left, mid, right)
    return invCount

arr = [2, 5, 1, 3, 4]
n = len(arr)
ans = mergeSort(arr, 0, n - 1)
print(ans)