class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            ans = pow(2, i)
            if (ans == n):
                return True
        return False


answer = Solution().isPowerOfTwo(128)
print(answer)
