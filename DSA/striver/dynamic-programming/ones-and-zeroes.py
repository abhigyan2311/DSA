from cmath import inf
from typing import List


class Solution:
    # Recursion - O(L)+O(2^L), O(N)
    # def computeMaxForm(self, i: int, counterPairs: List[(int)], m: int, n: int) -> int:
    #     # Base Case
    #     if i == 0:
    #         zeros, ones = counterPairs[0]
    #         if m-zeros >= 0 and n-ones >= 0: return 1
    #         return 0

    #     #Take
    #     take = -inf
    #     zeros, ones = counterPairs[i]
    #     if m-zeros >= 0 and n-ones >= 0:
    #         take = 1 + self.computeMaxForm(i-1, counterPairs, m-zeros, n-ones)
    #     # Not Take
    #     notTake = 0 + self.computeMaxForm(i-1, counterPairs, m, n)
    #     return max(take, notTake)

    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     l = len(strs)
    #     counterPairs = []
    #     for s in strs:
    #         zeros = s.count("0")
    #         ones = s.count("1")
    #         counterPairs.append((zeros, ones))
    #     return self.computeMaxForm(l-1, counterPairs, m, n)
    
    # Memoization - O(L*m*n), O(L*m*n) + O(N)
    # def computeMaxForm(self, i: int, counterPairs: List[(int)], m: int, n: int, dp: List[List[List[int]]]) -> int:
    #     # Base Case
    #     if i == 0:
    #         zeros, ones = counterPairs[0]
    #         if m-zeros >= 0 and n-ones >= 0: return 1
    #         return 0

    #     if dp[i][m][n] != -1: return dp[i][m][n]
    #     #Take
    #     take = -inf
    #     zeros, ones = counterPairs[i]
    #     if m-zeros >= 0 and n-ones >= 0:
    #         take = 1 + self.computeMaxForm(i-1, counterPairs, m-zeros, n-ones)
    #     # Not Take
    #     notTake = 0 + self.computeMaxForm(i-1, counterPairs, m, n, dp)
    #     dp[i][m][n] = max(take, notTake)
    #     return dp[i][m][n]

    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     l = len(strs)
    #     counterPairs = []
    #     for s in strs:
    #         zeros = s.count("0")
    #         ones = s.count("1")
    #         counterPairs.append((zeros, ones))
    #     dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(l)]
    #     return self.computeMaxForm(l-1, counterPairs, m, n, dp)
    
    # Tabulation - O(L*m*n), O(L*m*n)
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        counterPairs = []
        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")
            counterPairs.append((zeros, ones))

        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(l)]
        
        # Base Case
        zeros, ones = counterPairs[0]
        for j in range(zeros, m+1):
            for k in range(ones, n+1):
                dp[0][j][k] = 1
        
        for i in range(1, l):
            zeros, ones = counterPairs[i]
            for j in range(m+1):
                for k in range(n+1):
                    #Take
                    take = -inf
                    if j-zeros >= 0 and k-ones >= 0:
                        take = 1 + dp[i-1][j-zeros][k-ones]
                    # Not Take
                    notTake = 0 + dp[i-1][j][k]
                    dp[i][j][k] = max(take, notTake)
        return dp[l-1][m][n]
 
ans = Solution().findMaxForm(["10","0","1"], 1, 1)
print(ans)