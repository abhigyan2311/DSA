from typing import List

class Solution:
    def recSubset(self, i: int, arr: List[int], summ: int, ans: int) -> int:
        if i == len(arr): 
            ans.append(summ)
            return
        
        summ += arr[i]
        self.recSubset(i+1, arr, summ, ans)
        summ -= arr[i]
        self.recSubset(i+1, arr, summ, ans)

    def subsetSums(self, arr: List[int], N: int) -> List[int]:
        ans = []
        self.recSubset(0, arr, 0, ans)
        return ans

ans = Solution().subsetSums([5,2,1], 3)
print(ans)
