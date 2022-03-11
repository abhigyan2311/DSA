from typing import List

# Complexity - O(n2), O(1)

def selectionSort(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

ans = selectionSort([2, 5,3,6,1])
print(ans)