class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = 1
        if (x < 0):
            sign = -1
            x = x * sign
        while(x != 0):
            d = x % 10
            if ((a > INT_MAX/10) or (a < INT_MIN/10)):
                return 0
            a = (a * 10) + d
            x = x // 10
        return a * sign


answer = Solution().reverse(-123)
print(answer)
