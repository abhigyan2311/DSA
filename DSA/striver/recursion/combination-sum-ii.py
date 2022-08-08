from typing import List


class Solution:
    def findCombinations(self, index: int, target: int, candidates: List[int], ds: List[int], ans: List[List[int]]):
        if index == len(candidates):
            if target == 0: ans.append(ds[:])
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]: continue
            toPick = candidates[i]
            if toPick > target: break
            ds.append(toPick)
            self.findCombinations(i+1, target-toPick, candidates, ds, ans)
            ds.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Recursion - O(2^n) * k(avg length of every combination), O(k * x) ignoring auxiliary space used by recursion
        candidates.sort()
        ans = []
        self.findCombinations(0, target, candidates, [], ans)
        return ans
        