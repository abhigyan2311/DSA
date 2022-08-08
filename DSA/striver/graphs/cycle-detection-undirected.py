from typing import List

class SolutionBFS:
    def checkForCycle(self, node, visited: List[int], adj: List[List[int]]) -> bool:
        q = []
        q.append((node, -1))
        visited[node] = True
        while len(q) > 0:
            nextNode, parentNode = q.pop(0)
            for adjNode in adj[nextNode]:
                if not visited[adjNode]:
                    q.append((adjNode, nextNode))
                    visited[adjNode] = True
                elif adjNode != parentNode:
                    return True
        return False

    def cycleDetection(self, edges: List[List[int]], N: int, M: int) -> bool:
        if not edges: return False

        adj = [[] for _ in range(N+1)]
        for e in edges:
            if e[0] not in adj[e[1]]: adj[e[1]].append(e[0])
            if e[1] not in adj[e[0]]: adj[e[0]].append(e[1])
        visited = [False] * (N+1)
        for i in range(1,N+1):
            if not visited[i]:
                if self.checkForCycle(i, visited, adj): return True
        return False

class SolutionDFS:
    def checkForCycle(self, nodeT, visited: List[int], adj: List[List[int]]) -> bool:
        node, prev = nodeT
        visited[node] = True
        for adjNode in adj[node]:
            if not visited[adjNode]:
                if self.checkForCycle((adjNode, node), visited, adj): return True
            elif adjNode != prev:
                return True
        return False

    def cycleDetection(self, edges: List[List[int]], N: int, M: int) -> bool:
        if not edges: return False

        adj = [[] for _ in range(N+1)]
        for e in edges:
            if e[0] not in adj[e[1]]: adj[e[1]].append(e[0])
            if e[1] not in adj[e[0]]: adj[e[0]].append(e[1])
        visited = [False] * (N+1)
        for i in range(1,N+1):
            if not visited[i]:
                if self.checkForCycle((i,-1), visited, adj): return True
        return False


def cycleDetection(edges, n, m):
    return "Yes" if SolutionDFS().cycleDetection(edges, n, m) else "No"