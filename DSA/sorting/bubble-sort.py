from typing import List

# Complexity - O(n2), O(1)

def bubbleSort(arr: List[int]) -> List[int]:
    n = len(arr) - 1
    for i in range(n):
        swap = False
        for j in range(n - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    return arr

ans = bubbleSort([1,2,3,5,4])
print(ans)