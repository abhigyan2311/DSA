from heapq import heappop, heappush
from math import inf

class Solution:
    # def spanningTree(self, V, adj):
    #     parent = [-1]*V
    #     key = [inf] * V
    #     mstSet = [False]*V

    #     key[0] = 0

    #     for _ in range(V-1):
    #         mini = inf
    #         u = -1
    #         for v in range(V):
    #             if not mstSet[v] and key[v] < mini:
    #                 mini = key[v]
    #                 u = v
    #         mstSet[u] = True

    #         for adjNode in adj[u]:
    #             v, weight = adjNode[0], adjNode[1]
    #             if not mstSet[v] and weight < key[v]:
    #                 parent[v] = u
    #                 key[v] = weight
        
    #     return sum(key)
    
    def spanningTree(self, V, adj):
        parent = [-1]*V
        key = [inf] * V
        mstSet = [False]*V
        key[0] = 0
        pq = []
        heappush(pq, (0, 0))

        while pq:
            u = heappop(pq)[1]
            mstSet[u] = True

            for adjNode in adj[u]:
                v, weight = adjNode
                if not mstSet[v] and weight < key[v]:
                    parent[v] = u
                    heappush(pq, (weight, v))
                    key[v] = weight
        
        return sum(key)

ans = Solution().spanningTree(3, [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]])                
print(ans)
                    