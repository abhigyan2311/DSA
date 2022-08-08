# https://leetcode.com/problems/combination-sum/
# https://youtu.be/OyZFFqQtu98

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Recursion - O(2^t * k), O(k*x)
        def recCombSum(i, target, arr):
            if i == len(candidates):
                if target == 0:
                    ans.append(arr[:])
                return
            pickedEl = candidates[i]
            if pickedEl <= target:
                arr.append(pickedEl)
                recCombSum(i, target - pickedEl, arr)
                arr.pop()
            recCombSum(i+1, target, arr)
        
        ans = []
        recCombSum(0, target, [])
        return ans

ans = Solution().combinationSum([2,3,6,7], 7)
print(ans)

        