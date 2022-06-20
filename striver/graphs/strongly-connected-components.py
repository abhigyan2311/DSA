class Solution:
    def dfs(self, node, visited, st, adj):
        visited.add(node)
        for adjNode in adj[node]:
            if adjNode not in visited:
                self.dfs(adjNode, visited, st, adj)
        st.append(node)

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

ans = Solution().stronglyConnectedComponents(5, [[3,1],[1, 4], [3, 4], [1, 2], [4, 3], [0, 2], [0, 4]])

# def stronglyConnectedComponents(n, edges):