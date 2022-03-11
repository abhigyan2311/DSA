from typing import List

# Complexity - O(n2), O(n)

def insertionSort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        current = arr[i]
        j = i-1
        while j>=0 and current < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = current
    return arr

ans = insertionSort([7,2,3,5,1])
print(ans)