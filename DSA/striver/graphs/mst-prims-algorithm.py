from heapq import heappop, heappush
from math import inf

class Solution:
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # Initialize 3 lists parent, weights and mstSet
        parent = [-1]*V
        weights = [inf]*V
        mstSet = [False]*V

        # Starting with 0th vertex
        weights[0] = 0
        pq = [(0, 0)]
        ans = 0

        # There will be V-1 edges thus running counter V-1 times
        for _ in range(V):
            wt, u = heappop(pq)

            # Marking current node as visited
            mstSet[u] = True
            ans += wt

            # Checking all adj nodes of current node
            for nei in adj[u]:
                v, wt = nei
                # If not visited and weigth is less than existing weigth -> Update
                if mstSet[v] == False and wt < weights[v]:
                    weights[v] = wt
                    parent[v] = u
                    heappush(pq, (wt, v))
        return ans

ans = Solution().spanningTree(3, [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]])                
print(ans)
                    