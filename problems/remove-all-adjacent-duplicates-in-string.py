# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Brute Force - O(n*m), O(1)
        # def checker(s: str) -> int:
        #     for i in range(len(s)-1):
        #         if s[i] == s[i+1]:
        #             return i
        #     return -1

        # while True:
        #     chk = checker(s)
        #     if chk == -1:
        #         break
        #     s = s.replace(f'{s[chk]}{s[chk+1]}', '', 1)
        # return s

        # Stack - O(n), O(n)
        res = []
        for ch in s:
            if res and res[-1] == ch:
                res.pop()
            else:
                res.append(ch)
        return "".join(res)


ans = Solution().removeDuplicates('abbaca')
print(ans)