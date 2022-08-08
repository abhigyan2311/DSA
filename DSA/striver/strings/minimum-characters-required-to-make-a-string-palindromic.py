class Solution:
    def solve(self, A):
        k = len(A)
        s = A + '#' + A[::-1]
        print(s)
        n = len(s)
        
        lps = [0]*n
        prevLps, i = 0, 1

        while i < n:
            if s[i] == s[prevLps]:
                lps[i] = prevLps + 1
                prevLps += 1
                i += 1
            elif prevLps == 0:
                i += 1
            else:
                prevLps = lps[prevLps-1]
        print(lps)
        return k-lps[-1]

ans = Solution().solve("ABC")
print(ans)
