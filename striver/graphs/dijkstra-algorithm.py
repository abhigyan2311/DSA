from math import inf
from heapq import heappop, heappush

class Solution:
    def dijkstra(self, V, adj, S):
        minPq = []
        distTo = [inf] * V

        distTo[S] = 0
        heappush(minPq, [0, S])

        while minPq:
            prevDist, prevNode = heappop(minPq)
            for adjNode in adj[prevNode]:
                nextNode, nextDist = adjNode
                newDist = prevDist + nextDist
                if distTo[nextNode] > newDist:
                    distTo[nextNode] = newDist
                    heappush(minPq, [newDist, nextNode])
        return distTo


adj = [[[1, 9]], [[0, 9]]]
V = 2
S = 0
ans = Solution().dijkstra(V, adj, S)
print(ans)
        