import heapq
from typing import Counter, List


class Solution:
    # O(NlogK), O(k)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     c = Counter(nums).most_common(k)
    #     res = []
    #     for e in c:
    #         res.append(e[0])
    #     return res

    # TC - Nlogk, SC - O(N)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     c = Counter(nums)
    #     hp = []
    #     for key, val in c.items():
    #         heapq.heappush(hp, (-val, key))
    #     res = []
    #     for _ in range(k):
    #         res.append(heapq.heappop(hp)[1])
    #     return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freqArr = [[] for _ in range(len(nums) + 1)]

        for num, count in counter.items():
            freqArr[count].append(num)

        res = []
        for i in range(len(freqArr)-1, 0, -1):
            for el in freqArr[i]:
                res.append(el)
            if len(res) == k:
                break
        return res


ans = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(ans)
