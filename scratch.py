from re import L
from typing import List

class Solution:
    def reverse(self, l: List[str], left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
    
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
        self.reverse(s, 0, len(s) - 1)
        self.reverseWord(s)
        print(s)

Solution().reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])
