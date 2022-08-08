from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recCombSum(i, target, arr):
            if i == len(candidates):
                if target == 0: ans.append(arr[:])
                return
            
            pickedEl = candidates[i]
            if pickedEl <= target:
                arr.append(pickedEl)
                recCombSum(i, target-pickedEl, arr)
                arr.pop()
            recCombSum(i+1, target, arr)
        
        ans = []
        recCombSum(0, target, [])
        return ans