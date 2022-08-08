from typing import List
import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # Creating a heap
        heap = nums.copy()
        heapq.heapify(heap)

        # Incrementing the smallest element until k
        while k > 0:
            current = heapq.heappop(heap)
            heapq.heappush(heap, current+1)
            k -= 1
        
        # Multiply the heap
        ans = 1
        while len(heap) > 0:
            x = heapq.heappop(heap)
            ans = (ans * x)%(10**9+7)
        return ans

ans = Solution().maximumProduct([9,7,8], 9)
print(ans)