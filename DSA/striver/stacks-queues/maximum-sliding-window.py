from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i in range(len(nums)):
            # When sliding windows, remove the element out of the window of the start
            if dq and dq[0] == i-k:
                dq.popleft()
            # Making sure deque is maintained in an increasing order
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans


ans = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(ans)
