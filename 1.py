from typing import List, Tuple

class Solution:
    def findBridges(self, currNode: int, parentNode: int, currTime: int, visited: List[bool], tin: List[int], low: List[int], bridges: List[Tuple[int, int]], graph: List[List[int]]):
        visited[currNode] = True
        currTime += 1
        tin[currNode] = low[currNode] = currTime

        for adjNode in graph[currNode]:
            if adjNode == parentNode: continue
            if not visited[adjNode]:
                self.findBridges(adjNode, currNode, currTime, visited, tin, low, bridges, graph)
                low[currNode] = min(low[currNode], low[adjNode])
                if low[adjNode] > tin[currNode]: bridges.append((adjNode, currNode))
            else:
                low[currNode] = min(low[currNode], tin[adjNode])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        n = len(graph)
        bridges = []
        visited = [False]*n
        tin = [0]*n # Time Of Insertion
        low = [0]*n # Lowest Time
        currentTime = 0
        for i in range(n):
            self.findBridges(i, -1, currentTime, visited, tin, low, bridges, graph)
        return bridges

