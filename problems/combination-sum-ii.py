# https://leetcode.com/problems/combination-sum-ii/
# https://youtu.be/G1fRTGRxXU8

from typing import List

class Solution:
    def findCombinations(self, index: int, target: int, candidates: List[int], ds: List[int], ans: List[List[int]]):
        if target == 0:
            ans.append(ds[:])
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            ds.append(candidates[i])
            self.findCombinations(i+1, target - candidates[i], candidates, ds, ans)
            ds.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Recursion - O(2^n) * k(avg length of every combination), O(k * x) ignoring auxiliary space used by recursion
        candidates.sort()
        ans = []
        self.findCombinations(0, target, candidates, [], ans)
        return ans


ans = Solution().combinationSum2([10,1,2,7,6,1,5], 8)
print(ans)

        