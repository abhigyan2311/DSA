from math import ceil
from re import A


class Solution:
    #TC - O(N^2), SC- O(k)
    # def repeatedStringMatch(self, a: str, b: str) -> int:
    #     temp = ""
    #     count = 0
    #     while len(temp) < len(a) + len(b):
    #         temp += a
    #         count += 1
    #         if b in temp:
    #             return count
    #     return -1

    #RKMP
    def repeatedStringMatch(self, a: str, b: str) -> int:
        maxPossible = ceil(len(b)/len(a)) + 1
        endIdx = self.rkStringMatch(a*maxPossible, b)
        if(endIdx == -1): return -1
        return (maxPossible - (len(a)*maxPossible-endIdx)//len(a))

    def rkStringMatch(self, strng, pat):
        n = len(strng)
        m = len(pat)
        
        # Compute Pattern Hash
        patHash = self.computeHash(pat, m)

        # Traverse String and compute hash for length m
        strHash = 0
        i = 0
        while i < n-m+1:
            if i==0:
                strHash = self.computeHash(strng, m)
            else:
                strHash -= ord(strng[i-1]) * (10**(m-1))
                strHash *= 10
                strHash += ord(strng[i+m-1])
                strHash %= (2**31)
            if strHash == patHash:
                print("MATCHHH")
                return i+m
            i += 1
        return -1

    def computeHash(self, s, n):
        mod = 2**31
        strhash = 0
        for i in range(n):
            toPower = 10**(n-i-1)
            strhash += ord(s[i]) * toPower
        strhash %= mod
        return strhash

ans = Solution().repeatedStringMatch("abc", "cabcabca")
print(ans)
            