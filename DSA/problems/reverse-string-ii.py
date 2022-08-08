class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Direct - O(n), O(n)
        a = list(s)
        for i in range(0,len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return ''.join(a)

ans = Solution().reverseStr("abcdefg", 2)
print(ans)