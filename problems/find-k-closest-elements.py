from bisect import bisect_left
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Approach 1: Sort With Custom Comparator
        # sortedArr = sorted(arr, key = lambda num: abs(x - num))
        # arr.sort(key=lambda n:abs(x-n))
        # res = []
        # for i in range(k):
        #     res.append(arr[i])
        # return sorted(res)

        # Approach 2: Binary Search + Sliding Window
        # if len(arr) == k:
        #     return arr

        # mid = bisect_left(arr, x)
        # left = mid - 1
        # right = mid

        # while (right - left - 1) < k:
        #     if left == -1:
        #         right += 1
        #         continue
        #     if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
        #         left -= 1
        #     else:
        #         right += 1
        # return arr[left + 1:right]

        # Approach 3: Binary Search + Sliding Window (without bisect_left)
        # lo, hi = 0, len(arr) - 1
        # mid = 0
        # while (lo <= hi):
        #     mid = (lo + hi)//2
        #     if (arr[mid] == x):
        #         break
        #     elif (arr[mid] < x):
        #         lo = mid + 1
        #     else:
        #         hi = mid - 1
    
        # if mid > 0:
        #     l = mid - 1
        #     r = mid
        # else:
        #     l = mid
        #     r = mid + 1
        # while (r - l - 1) < k:
        #     if r == len(arr) or abs(arr[l] - x) <= abs(arr[r] - x):
        #         l -= 1
        #     else:
        #         r += 1
        # return arr[l+1:r]
        
        # Approach 3: Binary Search To Find The Left Bound
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
            
        
answer = Solution().findClosestElements([1,2,3,4,5,6,7,8], 3, 4)
print(answer)