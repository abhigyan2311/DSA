from collections import deque
from typing import List

class SolutionBFS:
    def cycleDetection(self, edges: List[List[int]], N: int) -> bool:
        if not edges: return False

        adj = [[] for _ in range(N+1)]
        for e in edges:
            adj[e[0]].append(e[1])

        topo = []
        indegree = [0]*(N+1)
        for i in range(1, N+1):
            for adjN in adj[i]:
                indegree[adjN] += 1
        
        q = deque()
        for i in range(1, N+1):
            if indegree[i] == 0:
                q.append(i)
        
        while len(q) > 0:
            node = q.popleft()
            topo.append(node)
            for adjN in adj[node]:
                indegree[adjN] -= 1
                if indegree[adjN] == 0: q.append(adjN)
        return not len(topo) == N

class SolutionDFS:
    def checkForCycle(self, node, visited: List[int], dfsVisited: List[int], adj: List[List[int]]) -> bool:
        visited[node] = True
        dfsVisited[node] = True
        for adjNode in adj[node]:
            if not visited[adjNode]:
                if self.checkForCycle(adjNode, visited, dfsVisited, adj): return True
            elif dfsVisited[adjNode]:
                return True
        dfsVisited[node] = False
        return False

    def cycleDetection(self, edges: List[List[int]], N: int) -> bool:
        if not edges: return False

        adj = [[] for _ in range(N+1)]
        for e in edges:
            adj[e[0]].append(e[1])

        visited = [False] * (N+1)
        dfsVisited = [False] * (N+1)
        for i in range(1,N+1):
            if not visited[i]:
                if self.checkForCycle(i, visited, dfsVisited, adj): return True
        return False


def cycleDetection(edges, n):
    return SolutionDFS().cycleDetection(edges, n)


edges = [[1,2],[]]