from typing import List


class Solution:
    # Recursive - O(2^N * 2^M), O(N*M)
    # def computeLCS(self, i: int, j: int, text1: str, text2: str) -> int:
    #     # Base Case
    #     if i < 0 or j < 0: return 0
    #     # Both are equal
    #     if text1[i] == text2[j]:
    #         return 1 + self.computeLCS(i-1, j-1, text1, text2)
    #     else:
    #         return max(self.computeLCS(i-1, j, text1, text2), self.computeLCS(i, j-1, text1, text2))

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     n, m = len(text1), len(text2)
    #     return self.computeLCS(n-1, m-1, text1, text2)

    # Memoization - O(N*M), O(N*M) + O(N+M)
    # def computeLCS(self, i: int, j: int, text1: str, text2: str, dp: List[List[int]]) -> int:
    #     # Base Case
    #     if i < 0 or j < 0: return 0
    #     if dp[i][j] != -1: return dp[i][j]
    #     # Both are equal
    #     if text1[i] == text2[j]:
    #         dp[i][j] = 1 + self.computeLCS(i-1, j-1, text1, text2, dp)
    #     else:
    #         dp[i][j] = max(self.computeLCS(i-1, j, text1, text2, dp), self.computeLCS(i, j-1, text1, text2, dp))
    #     return dp[i][j]

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     n, m = len(text1), len(text2)
    #     dp = [[-1]*m for _ in range(n)]
    #     return self.computeLCS(n-1, m-1, text1, text2, dp)
    
    # Tabulation - O(N*M), O(N*M)
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     n, m = len(text1), len(text2)
    #     dp = [[0]*(m+1) for _ in range(n+1)]
    #     for i in range(1, n+1):
    #         for j in range(1, m+1):
    #             if text1[i-1] == text2[j-1]:
    #                 dp[i][j] = 1 + dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #     return dp[n][m]
    
    # Tabulation + Space Optimzation- O(N*M), O(M)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        prev = [0]*(m+1)
        for i in range(1, n+1):
            curr = [0]*(m+1)
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        return prev[m]

ans = Solution().longestCommonSubsequence("abcde", "ace")
print(ans)