from typing import List


class Solution:
    # Memoization - O(N*M), O(N*M), O(N+M)
    # def computeMinDistance(self, i: int, j: int, word1: str, word2: str, dp: List[List[int]]) -> int:
    #     if i<0: return j+1
    #     if j<0: return i+1
    #     if dp[i][j] != -1: return dp[i][j]
    #     # Both matching
    #     if word1[i] == word2[j]: 
    #         dp[i][j] = self.computeMinDistance(i-1, j-1, word1, word2, dp)
    #         return dp[i][j]
    #     # Not Matching
    #     insert = self.computeMinDistance(i, j-1, word1, word2, dp)
    #     delete = self.computeMinDistance(i-1, j, word1, word2, dp)
    #     replace = self.computeMinDistance(i-1, j-1, word1, word2, dp)
    #     dp[i][j] = 1 + min(insert, delete, replace)
    #     return dp[i][j]

    # def minDistance(self, word1: str, word2: str) -> int:
    #     n, m = len(word1), len(word2)
    #     dp = [[-1 for _ in range(m)] for _ in range(n)]
    #     return self.computeMinDistance(n-1, m-1, word1, word2, dp)
        
    # Tabulation - O(N*M), O(N*M)
    # def minDistance(self, word1: str, word2: str) -> int:
    #     n, m = len(word1), len(word2)
    #     dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    #     # Base Case
    #     for j in range(m+1): dp[0][j] = j
    #     for i in range(n+1): dp[i][0] = i

    #     for i in range(1, n+1):
    #         for j in range(1, m+1):
    #             if word1[i-1] == word2[j-1]: 
    #                 dp[i][j] = dp[i-1][j-1]
    #             else:
    #                 # Not Matching
    #                 insert = dp[i][j-1]
    #                 delete = dp[i-1][j]
    #                 replace = dp[i-1][j-1]
    #                 dp[i][j] = 1 + min(insert, delete, replace)
    #     return dp[n][m]

    # Tabulation + Space Optimization - O(N*M), O(2M)
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        prev = [0 for _ in range(m+1)]
        # Base Case
        for j in range(m+1): prev[j] = j

        for i in range(1, n+1):
            curr = [0 for _ in range(m+1)]
            curr[0] = i
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]: 
                    curr[j] = prev[j-1]
                else:
                    # Not Matching
                    insert = curr[j-1]
                    delete = prev[j]
                    replace = prev[j-1]
                    curr[j] = 1 + min(insert, delete, replace)
            prev = curr
        return prev[m]

ans = Solution().minDistance("intention", "execution")
print(ans)