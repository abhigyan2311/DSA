from typing import List

# O(NlogN)
def merge(arr: List[int], left: int, mid: int, right: int) -> None:
    leftArr = arr[left:mid+1]
    rightArr = arr[mid+1: right+1]

    # Two pointers for traversing the two halves
    i, j = 0, 0
    # Pointer to iterate on the main list
    k = left
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1
    
    # For the remaining values if left in any half
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1
    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1

# O(NlogN)
def mergeSort(arr: List[int], left: int, right: int):
    if left >= right:
        return

    mid = (left+right)//2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid+1, right)
    merge(arr, left, mid, right)

arr = [7,6,5,4,3,2,1]
mergeSort(arr, 0, len(arr)-1)
print(arr)