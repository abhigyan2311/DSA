# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

from random import randint


class Solution:
    num = 0

    def guess(self, i: int) -> int:
        if i > self.num:
            return -1
        elif i < self.num:
            return 1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        self.num = randint(1, n)
        print(self.num)
        # Brute Force
        # for i in range(n):
        #     if self.guess(i) == 0:
        #         return i
        # return n

        # Binary Search
        left, right = 1, n
        while left <= right:
            pivot = (left + right) // 2
            res = self.guess(pivot)
            if res == 0:
                return pivot
            elif res == -1:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


answer = Solution().guessNumber(10)
print(answer)
