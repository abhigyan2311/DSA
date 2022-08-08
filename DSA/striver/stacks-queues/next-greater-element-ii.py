from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge, st = [None]*n, []

        for i in  range(2*n-1, -1, -1):
            while st and st[-1] <= nums[i%n]:
                st.pop()
            if i<n:
                if st: nge[i%n] = st[-1]
                else: nge[i%n] = -1
            st.append(nums[i%n])

        return nge
    
ans = Solution().nextGreaterElements([1,2,3,4,3])
print(ans)