from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Sum Solution - O(n), O(n)
        hashmap = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hashmap:
                return sorted([i+1, hashmap[complement] + 1])
            hashmap[numbers[i]] = i
        
        # Optimal Solution - O(n), O(1)
        left, right = 0, len(numbers)-1
        while left < right:
            mySum = numbers[left] + numbers[right]
            if target == mySum:
                return [left+1, right+1]
            elif target > mySum:
                left += 1
            else:
                right -= 1
        return [-1,-1]
                