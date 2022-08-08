# https://leetcode.com/problems/permutation-in-string/
# https://leetcode.com/problems/permutation-in-string/discuss/498216/Python-3-easy-approaches-sorting-hashing-and-rolling-hash

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Approach 1: Sorting - O(l1logl1 + (l2-l1)l1logl1), O(l1)
        # if len(s1) > len(s2):
        #     return False
        # s1 = "".join(sorted(s1))
        # for i in range(len(s2)):
        #     test = "".join(sorted(s2[i:i+len(s1)]))
        #     if s1 in test:
        #         return True
        # return False

        # Approach 2: Hashmap -  O(n*k), O(1)
        # if len(s1) > len(s2):
        #     return False
        # s1Map = Counter(s1)
        # for i in range(len(s2)):
        #     test = s2[i:i+len(s1)]
        #     s2Map = Counter(test)
        #     if s1Map == s2Map:
        #         return True
        # return False

        # Approach 3: Rolling Hashmap(Sliding Window) - 
        # k = len(s1)
        # d1 = Counter(s1)
        # # initial window
        # window = s2[:k]
        # d2 = Counter(window)
        # # check the intial window 
        # if d1 == d2:
        #     return True

        # for i in range(len(s2)-k):
        #     # 1 - remove s2[i]
        #     if d2[s2[i]] == 1:
        #         del d2[s2[i]]
        #     elif d2[s2[i]] > 1:
        #         d2[s2[i]] -= 1
        #     # 2- add s2[i+k]
        #     if s2[i+k] in d2:
        #         d2[s2[i+k]] += 1
        #     else:
        #         d2[s2[i+k]] = 1
        #     # check after sliding
        #     if d1 == d2:
        #         return True
        # return False

        # Approach 4: Array
        mapArr = [0] * 26
        for c in s1:
            mapArr[ord(c) - ord('a')] += 1
            
        i, j, countChars = 0, 0, len(s1)
        while j < len(s2):
            s2ArrStartIndex = ord(s2[i]) - ord('a')
            s2ArrEndIndex = ord(s2[j]) - ord('a')
            if mapArr[s2ArrEndIndex] > 0:
                countChars -= 1
            mapArr[s2ArrEndIndex] -= 1
            j += 1
            if countChars == 0:
                return True
            if j - 1 == len(s1):
                if mapArr[s2ArrStartIndex] >= 0:
                    countChars += 1
                mapArr[s2ArrStartIndex] += 1
                i += 1
        return False

ans = Solution().checkInclusion("ab", 'eidoooba')
print(ans)