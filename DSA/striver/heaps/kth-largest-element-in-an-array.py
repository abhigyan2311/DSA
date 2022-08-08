from heapq import heapify, heappop, heappush, _heapify_max, _heappop_max
from typing import List

class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     _heapify_max(nums)
    #     ans = None
    #     for _ in range(k):
    #         ans = _heappop_max(nums)
    #     return ans

    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heappush(minHeap, num)
            if len(minHeap) > k:
                heappop(minHeap)
        return heappop(minHeap)

ans = Solution().findKthLargest([3,2,1,5,6,4], 2)
print(ans)