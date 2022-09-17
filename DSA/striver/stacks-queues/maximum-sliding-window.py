from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i in range(nums):
            # If sliding window is ahead of current el in dq
            if dq and dq[0] == i-k:
                dq.popleft()

            # If dq is not maintained in decreasing order
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Append current index in dq
            dq.append(i)

            # Add to ans
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans


ans = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(ans)
