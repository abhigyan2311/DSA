class Solution:
    def ifKnows(self, M, a, b):
        if M[a][b] == 1: return True
        else: return False

    def celebrity(self, M, n):
        # Push everyone into a stack
        st = [] 
        for i in range(n):
            st.append(i)
        
        # Compare two elements if they know each other
        while len(st) > 1:
            a = st.pop()
            b = st.pop()
            if self.ifKnows(M, a, b):
                st.append(b)
            else: 
                st.append(a)
        
        # Potential Candidate
        c = st.pop()

        #Check Row
        for i in range(n):
            if M[c][i] != 0: return -1
        
        #Check Column
        for i in range(n):
            if c==i: continue
            if M[i][c] != 1: return -1
        
        return c

ans = Solution().celebrity([[0, 1, 0], [0, 0, 0], [0, 1, 0]], 3)
print(ans)
            