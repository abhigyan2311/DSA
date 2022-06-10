from cmath import inf
from collections import deque

class Solution:
    #TC - O(N^2), O(2N)
    # def maxOfMin(self,arr,n):
    #     # Iterate through window sizes from 1->N
    #     ans = []
    #     for w in range(1, n+1):
    #         dq = deque()
    #         maxi = -inf
    #         for i in range(n):
    #             if dq and dq[0][0] == i-w:
    #                 dq.popleft()
    #             while dq and dq[-1][1] > arr[i]:
    #                 dq.pop()
    #             dq.append((i, arr[i]))
    #             if i>=w-1:
    #                 maxi = max(maxi, dq[0][1])
    #         ans.append(maxi)
    #     return ans

    def maxOfMin(self,arr,n):
        lse, rse = [-1]*n, [n]*n

        # Compute left next smaller element array
        st = []
        for i in range(n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st: lse[i] = st[-1]
            st.append(i)
        
        # Compute right next smaller element array
        st = []
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st: rse[i] = st[-1]
            st.append(i)

        maxi = [0]*n
        for i in range(n):
            maxWindowSize = rse[i]-lse[i]-2
            maxi[maxWindowSize] = max(maxi[maxWindowSize], arr[i])

        for i in range(n-2, -1, -1):
            maxi[i] = max(maxi[i], maxi[i+1])
        return maxi
        

ans = Solution().maxOfMin([10,20,30,50,10,70,30], 7)
print(ans)