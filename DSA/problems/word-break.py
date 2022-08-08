from typing import List


class Solution:
    def recWordBreak(self, i: int, s: str, wordDict: List[str]) -> bool:
        if i==len(s): return True
        
        for x in range(i, len(s)):
            ss = s[i: x+1]
            if s[i: x+1] in wordDict and self.recWordBreak(x+1, s, wordDict):
                return True
        return False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.recWordBreak(0, s, wordDict)


ans = Solution().wordBreak("leetcode", ["leet", "code"])
print(ans)
        