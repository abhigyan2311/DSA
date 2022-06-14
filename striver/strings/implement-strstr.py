class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle == "": return 0

        # h = len(haystack)
        # n = len(needle)

        # for i in range(h-n+1):
        #     for j in range(n):
        #         print(haystack[i+j])
        #         if haystack[i+j] != needle[j]:
        #             break
        #         if j == len(needle)-1:
        #             return i

        if needle == "": return 0

        h = len(haystack)
        n = len(needle)

        # Compute LPS - O(2N)
        lps = [0]*n
        prevLps, i = 0, 1
        while i < n:
            if needle[i] == needle[prevLps]:
                lps[i] = prevLps + 1
                prevLps += 1
                i += 1
            elif prevLps == 0:
                lps[i] = 0
                i += 1
            else:
                prevLps = lps[prevLps-1]
        
        # KMP
        i = 0 # ptr for haystack
        j = 0 # ptr for needle

        while i < h:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == n:
                return i-n
        return -1


ans = Solution().strStr("hello", "bba")
print(ans)