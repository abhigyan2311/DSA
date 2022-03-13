# https://leetcode.com/problems/reverse-string/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Approach 1: Inbuilt function - O(n), O(1)
        # s.reverse()

        #Approach 2: Two Pointers - O(n), O(1)
        # i, j = 0, len(s) - 1
        # while i < j:
        #     s[i], s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1
        
        #Approach 3: Recursion - O(n), O(n)
        # def reverse(start, end):
        #     if start < end:
        #         s[start], s[end] = s[end], s[start]
        #         reverse(start + 1, end - 1)

        # reverse(0, len(s) - 1)

        # Approach 4: Pythonic
        s[:] = s[::-1]
        print(s)

Solution().reverseString(["h","e","l","l","o"])