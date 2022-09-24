from math import inf

class Solution:
    def bellman_ford(self, V, adj, S):
        distTo = [inf] * V
        distTo[S] = 0

        for _ in range(V-1):
            for u, v, wt in adj:
                distTo[v] = min(distTo[v], distTo[u] + wt)
        
        return distTo
