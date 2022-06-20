from typing import List


class Solution:

    def dfsOfGraph(self, V, adj):
        ans = []
        visited = [False] * (V)
        for i in range(V):
            if visited[i] == False:
                self.dfs(i, visited, adj, ans)
        return ans


    def dfs(self, node: int, visited: List[int], adj: List[List[int]], ans: List[int]):
        ans.append(node)
        visited[node] = True
        for adjNode in adj[node]:
            if visited[adjNode] == False:
                self.dfs(adjNode, visited, adj, ans)
