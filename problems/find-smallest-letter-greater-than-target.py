from bisect import bisect
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Approach 1: Linear Scan
        # for letter in letters:
        #     if letter > target:
        #         return letter
        # return letters[0]

        # Approach 2: Binary Search
        # if target >= letters[-1]: 
        #     return letters[0]
        # left, right = 0, len(letters) - 1
        # while left < right:
        #     mid = (left+right)//2
        #     if letters[mid] > target:
        #         right = mid
        #     else:
        #         left = mid + 1
        # return letters[left]

        # Approach 3: Binary Search with built in method
        index = bisect(letters, target)
        return letters[index % len(letters)]


answer = Solution().nextGreatestLetter(["c","f","j"], "c")
print(answer)