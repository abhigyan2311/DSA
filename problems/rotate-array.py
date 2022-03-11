from typing import List
from collections import deque

def rotateArray(nums: List[int], k: int) -> List[int]:
    # # Approach 1: Slicing - O(n), O(n)
    # k=k%len(nums)
    # nums[:] = nums[-k:] + nums[:-k]
    # return nums

    #Approach 2: Brute Force - O(n*k), O(1)
    # k = k%len(nums)
    # for _ in range(k):
    #     nums.insert(0, nums.pop())
    # return nums

    #Approach 3: Deque - O(k), O(n)
    # k = k%len(nums)
    # d = deque(nums)
    # for _ in range(k):
    #     d.appendleft(d.pop())
    # nums[:] = list(d)
    # return nums

    #Approach 4: Extra Array - O(n), O(n)
    # n = len(nums)
    # a = [0] * n
    # for i in range(n):
    #     a[(i + k) % n] = nums[i]
    # nums[:] = a
    # return nums

    #Approach 5: Reverse - O(n), O(1)
    def reverseInplace(nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    n = len(nums)
    k = k%n
    reverseInplace(nums, 0, n-1)
    reverseInplace(nums, 0, k-1)
    reverseInplace(nums, k, n-1)
    return nums
    
    

ans = rotateArray([1,2,3,4,5,6,7], 3)
print(ans)