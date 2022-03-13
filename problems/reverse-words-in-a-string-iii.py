from typing import List

class Solution:
    # Approach 1: Two Pointer Approach - O(n), O(1)
    def reverse(self, a: List[str], left: int, right: int) -> None:
        while left < right:
            a[left], a[right] = a[right], a[left]
            left, right = left+1, right-1

    def reverseWord(self, l: List[str]) -> str:
        n = len(l)
        start = end = 0
        while start < n:
            while end < n and l[end] != " ":
                end += 1
            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1
    
    # def reverseWords(self, s: str) -> str:
    #     a = list(s)
    #     self.reverseWord(a)
    #     return ''.join(a)
    
    # Approach 2: Pythonic - O(n)
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])[::-1]



ans = Solution().reverseWords("Let's take LeetCode contest")
print(ans)