class Solution:
    def findParent(self, u, parent):
        if u == parent[u]: 
            return u
        parent[u] = self.findParent(parent[u], parent)
        return parent[u]

    def unionn(self, u, v, parent, rank):
        u = self.findParent(u, parent)
        v = self.findParent(v, parent)
        if rank[u] < rank[v]:
            parent[u] = v
        elif rank[u] > rank[v]:
            parent[v] = u
        else:
            parent[v] = u 
            rank[u] += 1

    def spanningTree(self, V, adj):
        weightedAdj = []
        for u, adjEdges in enumerate(adj):
            for edge in adjEdges:
                weightedAdj.append((edge[1], u, edge[0]))
        weightedAdj.sort()
        
        parent = [i for i in range(V)]
        rank = [0]*V

        costMst = 0
        mstSet = []
        for adjNode in weightedAdj:
            wt, u, v = adjNode
            if self.findParent(u, parent) != self.findParent(v, parent):
                costMst += wt
                mstSet.append((u, v))
                self.unionn(u, v, parent, rank)
        return costMst

ans = Solution().spanningTree(3, [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]])                
print(ans)