from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Brute Force - O(2N + NlogN), O(N)
        # visited = set()
        # for i in range(len(nums)):
        #     visited.add(nums[i])
        # k = len(visited)
        # visited = sorted(visited)
        # for i, el in enumerate(visited):
        #     nums[i] = el
        # return k

        # Optimal - O(N), O(1)
        n = len(nums)
        if n == 0: return 0

        i = 0
        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1


ans = Solution().removeDuplicates([-1,0,0,0,0,3,3])
print(ans)
            
        
            