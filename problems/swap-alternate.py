from typing import List


class Solution:
    def swapAlternate(self, arr: List[int]) -> List[int]:
        for i in range(0, len(arr), 2):
            if (i+1 < len(arr)):
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
        return arr


answer = Solution().swapAlternate([5, 6, 8, 7, 1, 2])
print(answer)
