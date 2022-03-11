from typing import List


class Solution:
    def findUnique(self, arr: List[int]) -> int:
        ans = 0
        for i in range(0, len(arr)):
            ans = ans ^ arr[i]
        return ans


answer = Solution().findUnique([11, 22, 33, 33, 55, 22, 55])
print(answer)
