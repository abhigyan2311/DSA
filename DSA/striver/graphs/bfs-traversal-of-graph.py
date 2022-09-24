from collections import deque


class Solution:

    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        ans = []
        visited = [False]*V
        dq = deque()
        dq.append(0)
        visited[0] = True
        while dq:
            currV = dq.popleft()
            ans.append(currV)
            for nei in adj[currV]:
                if not visited[nei]:
                    dq.append(nei)
                    visited[nei] = True
        return ans


adjList = [[2, 5], [5, 6, 8], [], [4, 5], [7], [7], [], [], []]
ans = Solution().bfsOfGraph(len(adjList), adjList)
print(ans)
