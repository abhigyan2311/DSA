# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/636750/Java-or-C%2B%2B-or-Python3-or-Detailed-Explanation-or-O(N)-time

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        k = len(p)
        hm1 = Counter(p)
        
        # Initial Window
        window = s[:k]
        hm2 = Counter(window)
        if hm1 == hm2:
            ans.append(0)
        
        for i in range(len(s) - k):
            # Delete prvious index
            if hm2[s[i]] == 1:
                del hm2[s[i]]
            elif hm2[s[i]] > 1:
                hm2[s[i]] -= 1
                
            # Add next index
            if s[i+k] in hm2:
                hm2[s[i+k]] += 1
            else:
                hm2[s[i+k]] = 1
            
            if hm2 == hm1:
                ans.append(i+1)
        return ans
            

ans = Solution().findAnagrams("cbaebabacd", "abc")
print(ans)
            