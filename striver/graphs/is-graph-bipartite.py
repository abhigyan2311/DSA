import collections
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def bfs(i):
            q = collections.deque()
            q.append(i)
            color[i] = 1

            while q:
                node = q.popleft()
                for adjNode in graph[node]:
                    if color[adjNode] == -1:
                        color[adjNode] = 1-color[node]
                        q.append(adjNode)
                    elif color[adjNode] == color[node]: return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not bfs(i): return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        
        def dfs(node):
            if color[node] == -1: color[node] = 1
            for adjNode in graph[node]:
                if color[adjNode] == -1:
                    color[adjNode] = 1-color[node]
                    if not dfs(adjNode): return False
                elif color[adjNode] == color[node]: return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i): return False
        return True