class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Approach 1: Recursion(Can Overflow)
        # def recPow(x: float, n: int) -> float:   
        #     if (n == 0):
        #         return 1
        #     if (n == 1):
        #         return x
        #     xnm1 = recPow(x, n - 1)
        #     xn = x * xnm1
        #     return xn
        
        # if (n >= 0):
        #     return recPow(x,n)
        # else:
        #     return 1.0/recPow(x, -n)

        #Approach 2: Fast Power Recursion
        # def recPow(x: float, n: int) -> float:
        #     if (n == 0):
        #         return 1
        #     tmp = recPow(x, n // 2)
        #     res = tmp * tmp
        #     if (n % 2 == 1):
        #         res *= x
        #     return res
        
        # if (n >= 0):
        #     return recPow(x,n)
        # else:
        #     return 1.0/recPow(x, -n)

        #Approach 3: Fast Power Iteration
        def itePow(x: float, n: int) -> float:
            res = 1
            if (n == 0):
                return 1
            while (n > 0):
                if (n % 2 == 1):
                    res *= x
                    n -= 1
                else:
                    x = x * x
                    n //= 2
                
            return res
        
        if (n >= 0):
            return itePow(x,n)
        else:
            return 1.0/itePow(x, -n)

answer = Solution().myPow(2, 5)
print(answer)