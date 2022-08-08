# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

from random import randint


class Solution:
    badVersion = 1

    def isBadVersion(self, version: int) -> bool:
        return version >= self.badVersion

    def firstBadVersion(self, n: int) -> int:
        self.badVersion = randint(1, n)
        print(f"Bad Version: {self.badVersion}")

        left, right = 1, n
        while left <= right:
            mid = (left + right)//2
            if self.isBadVersion(mid):
                if self.isBadVersion(mid - 1):
                    right = mid - 1
                else:
                    return mid
            else:
                left = mid + 1
        return -1


answer = Solution().firstBadVersion(10)
print(answer)
