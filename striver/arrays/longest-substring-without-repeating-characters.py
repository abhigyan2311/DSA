from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Optimal 1 - O(2N), O(1)
        visited = set()
        length = 0
        l, r = 0, 0
        for r in range(len(s)):
            if s[r] in visited:
                while l < r and s[r] in visited:
                    visited.remove(s[l])
                    l += 1
            visited.add(s[r])
            length = max(length, r-l+1)
        return length

        # Optimal 2 - O(N), O(1)
        visited = {}
        length = 0
        l, r = 0, 0
        for r in range(len(s)):
            if s[r] in visited:
                    l = max(l, visited[s[r]] + 1)
            visited[s[r]] = r
            length = max(length, r-l+1)
        return length 
 

ans = Solution().lengthOfLongestSubstring("tmmzuxt")
print(ans)