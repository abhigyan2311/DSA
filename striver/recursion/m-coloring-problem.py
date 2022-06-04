# https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#

from typing import List

class Solution:
    # Optimal - O(N^M), O(N) + O(N){Auxiliary Space}
    def isValid(self, node: int, graph: List[List[int]], N: int, color: List[int], col: int):
        for k in range(N):
            if k != node and graph[node][k] == 1 and color[k] == col:
                return False
        return True

    def solve(self, node: int, graph: List[List[int]], m: int, N: int, color: List[int]):
        if node == N:
            return True
        for i in range(1, m+1):
            if self.isValid(node, graph, N, color, i):
                color[node] = i
                if self.solve(node+1, graph, m, N, color):
                    return True
                color[node] = 0
        return False

    def graphColoring(self, graph: List[List[int]], m: int, N: int) -> bool:
        color = [0] * N
        if self.solve(0, graph, m, N, color): 
            return True
        return False

ans = Solution().graphColoring([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]], 3, 4)
print(ans)