from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Intersection
        # return (set(nums1) & set(nums2))

        # Intersection 2
        # if len(nums1) > len(nums2):
        #     return set(nums1).intersection(nums2)
        # else:
        #     return set(nums2).intersection(nums1)

         # if the lists are already sorted and you're told to solve in O(n) time and O(1) space:
        nums1.sort() # assume sorted
        nums2.sort() # assume sorted

        # iterate both nums backwards till at least 1 is empty
        # if num2[j] > num1[i], pop num2
        # if num2[j] < num1[i], pop num1
        # if equal and num not last appended to result, append to result and pop both nums
        
        result = set()
                
        while nums1 and nums2:
            if nums2[-1] > nums1[-1]:
                nums2.pop()
            elif nums2[-1] < nums1[-1]:
                nums1.pop()
            else:
                # to avoid duplicates
                # if not result or nums1[-1] != result[-1]:
                result.add(nums1[-1])
                nums1.pop()
                nums2.pop()

        return list(result)
 
answer = Solution().intersection([1,2,2,1], [2,2])
print(answer)