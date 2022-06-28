from math import inf

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, adj, S):
        distTo = [100000000] * V
        distTo[S] = 0

        for _ in range(V-1):
            for u, v, wt in adj:
                distTo[v] = min(distTo[v], distTo[u] + wt)
        
        return distTo
