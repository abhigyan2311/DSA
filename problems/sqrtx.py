class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary Search
        if x < 2:
            return x

        left, right = 2, x//2
        while left <= right:
            pivot = (left + right)//2
            num = pivot * pivot
            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right

        # Newton's method
        # if x < 2:
        #     return x
        # r = x//2
        # while r*r > x:
        #     r = (r + x//r) // 2
        # return r


answer = Solution().mySqrt(25)
print(answer)
