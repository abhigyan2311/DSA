class Solution:
    def bitwiseComplement(self, n: int) -> int:
        while (n == 0):
            return 1
        m = n
        mask = 0
        while (m != 0):
            mask = (mask << 1) | 1
            m = m >> 1
        ans = mask ^ n
        return ans


answer = Solution().bitwiseComplement(5)
print(answer)
