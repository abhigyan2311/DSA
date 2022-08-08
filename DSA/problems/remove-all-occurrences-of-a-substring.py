# https://www.youtube.com/watch?v=V5-7GzOfADQ
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

from typing import List

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Approach 1: Built in function - O(m*n)
        # while part in s:
        #     s = s.replace(part, '', 1)
        # return s

        # Approach 2: Stack - O(m*n)
        stack = []
        for ch in s:
            stack.append(ch)
            print(stack[-len(part):])
            if "".join(stack[-len(part):]) == part:
                for _ in range(len(part)):
                    stack.pop()
        return "".join(stack)

        # Approach 3: KMP - O(n+m)
    #     if not part or not s: return s
    #     n, m = len(s), len(part)
    #     pr_arr = self.getPrefixArray(part)
    #     st = []
    #     i = j = 0
    #     while i < n:
    #         if part[j] == s[i]:
    #             st.append((s[i], j))
    #             i += 1
    #             j += 1
    #             if j == m:
    #                 for x in range(0, m):
    #                     st.pop(-1)
    #                 if st:
    #                     j = st[-1][1] + 1 # start matching from the unmatched index, before this part index, all chars have matched
    #                 else:
    #                     j = 0
    #         else:
    #             if j > 0:
    #                 j = pr_arr[j-1]
    #             else:
    #                 st.append((s[i], -1))
    #                 i+=1
    #     r = ""
    #     for i in st:
    #         r += i[0]
    #     return r

    # def getPrefixArray(self, part):
    #     lps, j = [0], 0
    #     for i in range(1, len(part)):
    #         if part[j] == part[i]:
    #             lps.append(j+1)
    #             j += 1
    #         else:
    #             while j >= 0:
    #                 j = lps[j-1]
    #                 if part[j] == part[i]:
    #                     lps.append(j+1)
    #                     j += 1
    #                     break
    #                 if j == 0 and part[j] != part[i]:
    #                     lps.append(0)
    #                     break
    #     return lps


ans = Solution().removeOccurrences('daabcbaabcbc', 'abc')
print(ans)