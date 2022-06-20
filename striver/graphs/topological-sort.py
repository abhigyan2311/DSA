from collections import deque

class Solution:
    def dfs(self, node, visited, st, adj):
        visited[node] = True
        for adjNode in adj[node]:
            if not visited[adjNode]:
                self.dfs(adjNode, visited, st, adj)
        st.append(node)

    # def topoSort(self, V, adj):
    #     visited = [False] * V
    #     st = []
    #     for i in range(V):
    #         if not visited[i]:
    #             self.dfs(i, visited, st, adj)
    #     return st[::-1]

    def topoSort(self, V, adj):
        topo = []
        indegree = [0]*V
        for i in range(V):
            for adjN in adj[i]:
                indegree[adjN] += 1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        while len(q) > 0:
            node = q.popleft()
            topo.append(node)
            for adjN in adj[node]:
                indegree[adjN] -= 1
                if indegree[adjN] == 0: q.append(adjN)
        return topo

adj = [[], [0], [0], [0]]
ans = Solution().topoSort(4, adj)
print(ans)