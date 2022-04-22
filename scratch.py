class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # while (n == 0):
        #     return 1
        # m = n
        # mask = 0
        # while (m != 0):
        #     mask = (mask << 1) | 1
        #     m = m >> 1
        # ans = mask ^ n
        # return ans

        if n <= 0:
            return 0
        nBinary = int(format(n, "b"))
        a = []
        while nBinary > 0:
            a.append(nBinary%10)
            nBinary //= 10
        
        ans = []
        for i in range(len(a) - 1, -1, -1):
            if a[i] == 0:
                ans.append("1")
            else:
                ans.append("0")
        res = "".join(ans)
        return int(res, 2)

ans = Solution().bitwiseComplement(0)
print(ans)

