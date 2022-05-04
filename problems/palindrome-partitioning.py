# https://leetcode.com/problems/palindrome-partitioning
# https://youtu.be/WBgsABoClE0
# https://youtu.be/wvaYrOp94k0

from typing import List

class Solution:
    # Recursion - O(2^n * n), O(n)
    def isPalindrome(self, s: str, start: int, end: int):
        return s[start: end+1] == s[start: end+1][::-1]

    def solve(self,  index: int, s: str, path: List[str], ans: List[List[str]]):
        if index == len(s):
            ans.append(path[:])
            return
        for x in range(index, len(s)):
            if self.isPalindrome(s, index, x):
                path.append(s[index: x+1])
                self.solve(x+1, s, path, ans)
                path.pop()


    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        self.solve(0, s, path, ans)
        return ans

ans = Solution().partition("aab")
print(ans)