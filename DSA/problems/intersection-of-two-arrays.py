# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Intersection
        # return list(set(nums1) & set(nums2))

        # BuiltIn method
        # if len(nums1) > len(nums2):
        #     return set(nums1).intersection(set(nums2))
        # else:
        #     return set(nums2).intersection(set(nums1))

         # if the lists are already sorted and you're told to solve in O(n) time and O(1) space:
        nums1.sort() # assume sorted
        nums2.sort() # assume sorted
        
        result = set()
        while nums1 and nums2:
            if nums2[-1] > nums1[-1]:
                nums2.pop()
            elif nums2[-1] < nums1[-1]:
                nums1.pop()
            else:
                result.add(nums1[-1])
                nums1.pop()
                nums2.pop()

        return list(result)
 
answer = Solution().intersection([1,2,2,1], [2,2])
print(answer)