from typing import List

class Solution:
    # Recursion - O(2^n) + (2^n)Log(2^n), O(n)
    def recSum(self, i: int, arr: List[int], mySum: int, ans: int):
        if i == len(arr):
            ans.append(mySum)
            return
        # Pick the element
        self.recSum(i+1, arr, mySum + arr[i], ans)
        # Do not pick the element
        self.recSum(i+1, arr, mySum, ans)

    def subsetSums(self, arr: List[int], N: int) -> List[int]:
        ans = []
        self.recSum(0, arr, 0, ans)
        ans.sort()
        return ans

ans = Solution().subsetSums([5, 2, 1], 3)
print(ans)