from math import inf
from typing import List

class Solution:
    # Recursion - O(2^N), O(N)
    # def computeMaxVal(self, ind: int, bagWeight: int, weights: List[int], values: List[int]) -> int:
    #     # Base Case
    #     if ind == 0:
    #         if weights[0] <= bagWeight: return values[0]
    #         return 0
    #     # Not Pick
    #     notTaken = 0 + self.computeMaxVal(ind-1, bagWeight, weights, values)
    #     # Pick
    #     taken = -inf
    #     if weights[ind] <= bagWeight:
    #         taken = values[ind] + self.computeMaxVal(ind-1, bagWeight-weights[ind], weights, values)
    #     return max(notTaken, taken)

    # def knapsack(self, weights: List[int], values: List[int], n: int, w: int) -> int:
    #     return self.computeMaxVal(n-1, w, weights, values)

    # Memoization - O(N*W), O(N*W) + O(N)
    # def computeMaxVal(self, ind: int, bagWeight: int, weights: List[int], values: List[int], dp: List[List[int]]) -> int:
    #     # Base Case
    #     if ind == 0:
    #         if weights[0] <= bagWeight: return values[0]
    #         return 0
    #     if dp[ind][bagWeight] != -1: return dp[ind][bagWeight]

    #     # Not Pick
    #     notTaken = 0 + self.computeMaxVal(ind-1, bagWeight, weights, values, dp)
    #     # Pick
    #     taken = -inf
    #     if weights[ind] <= bagWeight:
    #         taken = values[ind] + self.computeMaxVal(ind-1, bagWeight-weights[ind], weights, values, dp)
    #     dp[ind][bagWeight] = max(notTaken, taken)
    #     return dp[ind][bagWeight]

    # def knapsack(self, weights: List[int], values: List[int], n: int, w: int) -> int:
    #     dp = [[-1]*(w+1) for _ in range(n)]
    #     return self.computeMaxVal(n-1, w, weights, values, dp)
    
    # Tabulation - O(N*W), O(N*W)
    # def knapsack(self, weights: List[int], values: List[int], n: int, w: int) -> int:
    #     dp = [[0]*(w+1) for _ in range(n)]
    #     for j in range(weights[0], w+1): dp[0][j] = values[0]

    #     for i in range(1, n):
    #         for j in range(w+1):
    #             # Not Pick
    #             notTaken = 0 + dp[i-1][j]
    #             # Pick
    #             taken = -inf
    #             if weights[i] <= j:
    #                 taken = values[i] + dp[i-1][j-weights[i]]
    #             dp[i][j] = max(notTaken, taken)
    #     return dp[n-1][w]
    
    # Tabulation + Space Optimization - O(N*W), O(2W)
    # def knapsack(self, weights: List[int], values: List[int], n: int, w: int) -> int:
    #     prev = [0]*(w+1)
    #     for j in range(weights[0], w+1): prev[j] = values[0]

    #     for i in range(1, n):
    #         curr = [0]*(w+1)
    #         for j in range(w+1):
    #             # Not Pick
    #             notTaken = 0 + prev[j]
    #             # Pick
    #             taken = -inf
    #             if weights[i] <= j:
    #                 taken = values[i] + prev[j-weights[i]]
    #             curr[j] = max(notTaken, taken)
    #         prev = curr
    #     return prev[w]
    
    # Tabulation + More Space Optimization - O(N*W), O(W)
    def knapsack(self, weights: List[int], values: List[int], n: int, w: int) -> int:
        prev = [0]*(w+1)
        for j in range(weights[0], w+1): prev[j] = values[0]

        for i in range(1, n):
            for j in range(w, -1, -1):
                # Not Pick
                notTaken = 0 + prev[j]
                # Pick
                taken = -inf
                if weights[i] <= j:
                    taken = values[i] + prev[j-weights[i]]
                prev[j] = max(notTaken, taken)
        return prev[w]

ans = Solution().knapsack([3, 2, 5], [30, 40, 60], 3, 6)
print(ans)