from math import inf
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        lo, hi = 0, m
        medianPos = (m+n+1)//2
        while lo <= hi:
            cut1 = (lo+hi)//2
            cut2 = (medianPos) - cut1

            left1 = -inf if cut1 == 0 else nums1[cut1-1]
            left2 = -inf if cut2 == 0 else nums2[cut2-1]

            right1 = inf if cut1 == m else nums1[cut1]
            right2 = inf if cut2 == n else nums2[cut2]

            if left1 <= right2 and left2 <= right1:
                if (m+n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2))/2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                hi = cut1-1
            else:
                lo = cut1+1
        return 0


ans = Solution().findMedianSortedArrays([1, 2], [3, 4])
print(ans)
