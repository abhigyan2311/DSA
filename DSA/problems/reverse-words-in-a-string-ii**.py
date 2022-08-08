from typing import List
from collections import deque

class Solution:
    # Approach 1: Reverse the Whole String and Then Reverse Each Word - O(n), O(1)
    def reverse(self, l: List[str], left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left+1, right-1
        
    def reverseWord(self, l: List[str]) -> None:
        n = len(l)
        start = end = 0
        while start < n:
            while end < n and l[end] != " ":
                end += 1
            self.reverse(l, start, end - 1)
            start = end + 1
            end = start
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        self.reverseWord(s)
        return s
        

ans = Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
print(ans)