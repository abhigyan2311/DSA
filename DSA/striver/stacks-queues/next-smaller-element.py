class Solution:
    def prevSmaller(self, A):
        n = len(A)
        nse, st = [None]*n, []

        for i in range(n):
            while st and st[-1] >= A[i]:
                st.pop()
            if st: nse[i] = st[-1]
            else: nse[i] = -1
            st.append(A[i])
        
        return nse

ans = Solution().prevSmaller([4, 5, 2, 10, 8])
print(ans)
