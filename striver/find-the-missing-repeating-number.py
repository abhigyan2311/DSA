from math import log2
from typing import List

class Solution:
    def missingAndRepeating(self, arr: List[int], n: int) -> List[int]:
        # Brute force - O(2N), O(N)
        # ans = [-1] * 2
        # countArr = [0] * (n+1)
        # for num in arr:
        #     countArr[num] += 1
        # for i in range(1, n+1):
        #     if countArr[i] == 2:
        #         ans[0] = i
        #     if countArr[i] == 0:
        #         ans[1] = i
        # return ans

        # Optimal 1
        # arrSum = sum(arr)
        # actSum = (n * (n+1))//2
        # xMiny = actSum - arrSum

        # arrSqSum = sum(i*i for i in arr)
        # actSqSum = (n*(n+1)*(2*n+1))//6
        # x2Miny2 = actSqSum - arrSqSum

        # xPlusy = x2Miny2//xMiny
        # twicex = xPlusy + xMiny
        # x = twicex//2
        # y = x - xMiny
        # return (x, y)

        # Optimal 2
        x, y = 0, 0
        nXor = 0
        for i in range(1, n+1):
            nXor ^= i
        for num in arr:
            nXor ^= num
        rsb = nXor & -nXor
        for num in arr:
            if num & rsb:
                x ^= num
            else:
                y ^= num
        for i in range(1, n+1):
            if i & rsb:
                x ^= i
            else:
                y ^= i
        # Check if the result is inverted as it does not guarantee x will be missing and y repeating
        for num in arr:
            if x == num:
                return y, x
                
        return x, y

ans = Solution().missingAndRepeating([4,3,6,2,1,1], 6)
print(ans)
