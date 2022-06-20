from queue import Queue

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        ans = []
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                q = []
                q.append(i)
                while len(q)>0:
                    nextNode = q.pop(0)
                    ans.append(nextNode)
                    for adjNode in adj[nextNode]:
                        if not visited[adjNode]:
                            q.append(adjNode)
                            visited[adjNode] = True
        return ans

    
    def bfsOfGraph(self, V, adj):
        ans = []
        visited = [False] * V
        q = []
        q.append(0)
        visited[0] = True
        while len(q) != 0:
            nextNode = q.pop(0)
            ans.append(nextNode)
            for adjNode in adj[nextNode]:
                if visited[adjNode] == False:
                    q.append(adjNode)
                    visited[adjNode] = True
        return ans

adjList = [[2, 5], [5,6,8], [], [4,5], [7], [7], [], [], []]
ans = Solution().bfsOfGraph(len(adjList), adjList)
