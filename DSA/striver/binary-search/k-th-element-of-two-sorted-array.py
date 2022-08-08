from math import inf

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n > m: return self.kthElement(arr2, arr1, m, n, k)

        lo, hi = max(0, k-m), min(k,n)
        while lo<=hi:
            cut1 = (lo+hi)//2
            cut2 = k-cut1

            left1 = -inf if cut1==0 else arr1[cut1-1]
            left2 = -inf if cut2==0 else arr2[cut2-1]
            right1 = inf if cut1==n else arr1[cut1]
            right2 = inf if cut2==m else arr2[cut2]

            if left1<=right2 and left2<=right1: return max(left1, left2)
            elif left1 > right2:
                hi = cut1-1
            elif left2 > right1:
                lo = cut1+1
        return 1

ans = Solution().kthElement([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 5, 7, 7)
print(ans)