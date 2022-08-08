# https://leetcode.com/problems/valid-palindrome/

from re import L


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Approach 1: Two Pointer - O(n), O(1)
        # i, j = 0, len(s) - 1
        # while i < j:
        #     if not s[i].isalnum():
        #         i += 1
        #     elif not s[j].isalnum():
        #         j -= 1
        #     else:
        #         if s[i].lower() != s[j].lower():
        #             return False
        #         i, j = i+1, j-1
        # return True

        #Approach 2: Reverse String - O(n), O(n)
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]

ans = Solution().isPalindrome("race a car")
print(ans)