class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: return s

        longestPalStr = ""

        for i in range(n):
            odd = self.palindromeAt(s, i, i)
            even = self.palindromeAt(s, i, i+1)
            longestPalStr = max(longestPalStr, odd, even, key=len)
        return longestPalStr

    def palindromeAt(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

ans = Solution().longestPalindrome("ac")
print(ans)