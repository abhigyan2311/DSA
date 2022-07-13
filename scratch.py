from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.adj = defaultdict(list)
        self.eulerTour = []
        self.visited = [False]*10e4
        self.level = [0]*10e4
        self.indMap = {}
    
    def dfs(self, node: int, level=1):
        self.visited[node] = True
        self.eulerTour.append(node)
        self.level[node] = level
        for adjN in self.adj[node]:
            if not self.visited[adjN]:
                self.dfs(adjN, level+1)
        self.eulerTour.append(node)

    
    def solve(self, N, Q, Edge, query):
        # Construct the graph
        for ed in Edge:
            self.adj[ed[0]].append(ed[1])
            self.adj[ed[1]].append(ed[0])
        
        # DFS
        self.dfs(0)
        
        # Compute start and end indexes of euler tour
        for node in self.eulerTour:
            if inde
        

N = 2
Q = 2
edge = [[0, 1], [0, 2], [1, 3], [1, 4]]
query = [[0, 1], [1, 4]]

ans = Solution().solve(N, Q, edge, query)
print(ans)