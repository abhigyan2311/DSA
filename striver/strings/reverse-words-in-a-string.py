from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        # Approach 1: Built in method - O(n), O(n)
        # return " ".join(reversed(s.split()))

        # Approach 2: Deque
        left, right = 0, len(s) - 1

        while left<=right and s[left] == " ":
            left += 1
        while left<=right and s[right] == " ":
            right -= 1
        
        d, word = deque(), []
        while left <= right:
            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.appe nd(s[left])
            left += 1
        d.appendleft("".join(word))
        return ' '.join(d)

ans = Solution().reverseWords("the sky is blue")
print(ans)