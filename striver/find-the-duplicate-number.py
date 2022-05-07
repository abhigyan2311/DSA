# https://leetcode.com/problems/find-the-duplicate-number/
# https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode
# https://www.youtube.com/watch?v=32Ll35mhWg0&ab_channel=takeUforward
# https://youtu.be/oVa8DfUDKTw


from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force - O(nlogn), O(1)
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
        
        # Hashmap - O(n), O(n) 
        # hsmp = {} 
        # for i in range(len(nums)):
        #     if nums[i] in hsmp:
        #         return nums[i]
        #     else:
        #         hsmp[nums[i]] = 1
                
        # Floyd's Cycle Detection - O(n), O(1)
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

answer = Solution().findDuplicate([1, 3, 2, 3, 4] )
print(answer)
