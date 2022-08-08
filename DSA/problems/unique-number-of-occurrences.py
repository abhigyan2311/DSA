from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Manual - O(n)
        # dict = {}
        # for i in range(0, len(arr)):
        #     if (arr[i] in dict):
        #         dict[arr[i]] += 1
        #     else:
        #         dict[arr[i]] = 1
        # dictV = list(dict.values())

        # Built-in Counter - O(n)
        dictV = list(Counter(arr).values())

        if len(dictV) != len(set(dictV)):
            return False
        return True


ans = Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3])
print(ans)
