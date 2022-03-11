# https://leetcode.com/problems/valid-perfect-square/solution/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary Search
#         if num < 2:
#             return num

#         left, right = 2, num//2
#         while left <= right:
#             pivot = (left + right)//2
#             n = pivot * pivot
#             if n > num:
#                 right = pivot - 1
#             elif n < num:
#                 left = pivot + 1
#             else:
#                 return True
#         return False

        # Newton's method
        if (num < 2):
            return True
        r = num / 2
        while r*r > num:
            r = (r + num//r) // 2
        return (r * r == num)