class Solution:
    def AllPossibleStrings(self, s):
        n = len(s)
        ans = []
        numLimit = 2**n
        for num in range(1, numLimit):
            substr = ""
            for i in range(n):
                if (num & (1<<i)) !=0 :
                    substr += s[i]
            ans.append(substr)
        ans.sort()
        return ans

ans = Solution().AllPossibleStrings("abc")
print(ans)