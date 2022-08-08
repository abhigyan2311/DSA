class Solution:
    def dfs(self, node, visited, st, adj):
        visited.add(node)
        for adjNode in adj[node]:
            if adjNode not in visited:
                self.dfs(adjNode, visited, st, adj)
        st.append(node)
    
    def revDfs(self, node, visited, transposeAdj, ssc):
        visited.add(node)
        ssc.append(node)
        for adjNode in transposeAdj[node]:
            if adjNode not in visited:
                self.revDfs(adjNode, visited, transposeAdj, ssc)

    def stronglyConnectedComponents(self, n, edges):
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
        #Step 1: Sort all nodes in topological sorted way
        visited = set()
        st = []
        for i in range(n):
            if i not in visited:
                self.dfs(i, visited, st, adj)
        # Step 2: Transpose the graph
        transposeAdj = [[] for _ in range(n)]
        for i in range(n):
            for adjNode in adj[i]:
                transposeAdj[adjNode].append(i)
        # Step 3: Apply DFS 
        ans = []
        visited = set()
        while len(st) > 0:
            node = st.pop()
            if node not in visited:
                ssc = []
                ans.append(ssc)
                self.revDfs(node, visited, transposeAdj, ssc)
        return ans

def stronglyConnectedComponents(n, edges):
    return Solution().stronglyConnectedComponents(n, edges)