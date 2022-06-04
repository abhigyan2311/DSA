# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
# https://youtu.be/bLGZhJlt4y0

from typing import List

# O(4^(n*m)), O(n*m)
class Solution:
    # def solve(self, i: int, j: int, m: int, n: int, ans: List[str], move: str, visited: List[List[int]], di: List[int], dj: List[int]):
    #     if i == n-1 and j == n-1:
    #         ans.append(move)
    #         return

    #     directions = "DLRU"
    #     for x in range(4):
    #         nexti = i + di[x]
    #         nextj = j + dj[x]
    #         if nexti>=0 and nextj>=0 and nexti<n and nextj<n and visited[nexti][nextj]!=1 and m[nexti][nextj]==1:
    #             visited[i][j] = 1
    #             self.solve(nexti, nextj, m, n, ans, move + directions[x], visited, di, dj)
    #             visited[i][j] = 0

    def solve(self, i: int, j: int, m: int, n: int, ans: List[str], move: str, visited: List[List[int]], di: List[int], dj: List[int]):
        if i==n-1 and j==n-1:
            ans.append(move)
            return
        
        directions = "DLRU"
        for x in range(4):
            nexti = i + di[x]
            nextj = j + dj[x]
            if nexti>=0 and nextj>=0 and nexti<n and nextj<n and visited[nexti][nextj]!=1 and m[nexti][nextj]==1:
                visited[i][j] = 1
                self.solve(nexti, nextj, m, n, ans, move+directions[x], visited, di, dj)
                visited[i][j] = 0


    # def solve(self, i: int, j: int, m: int, n: int, ans: List[str], move: str, visited: List[List[int]]):
    #     if i==n-1 and j==n-1:
    #         ans.append(move)
    #         return

    #     # Downward
    #     if i+1<n and visited[i+1][j] != 1 and m[i+1][j] == 1:
    #         visited[i][j] = 1
    #         self.solve(i+1, j, m, n, ans, move+"D", visited)
    #         visited[i][j] = 0
    #     # Left
    #     if j-1>=0 and visited[i][j-1] != 1 and m[i][j-1] == 1:
    #         visited[i][j] = 1
    #         self.solve(i, j-1, m, n, ans, move+"L", visited)
    #         visited[i][j] = 0
    #     # Right
    #     if j+1<n and visited[i][j+1] != 1 and m[i][j+1] == 1:
    #         visited[i][j] = 1
    #         self.solve(i, j+1, m, n, ans, move+"R", visited)
    #         visited[i][j] = 0
    #     # Upward
    #     if i-1>=0 and visited[i-1][j] != 1 and m[i-1][j] == 1:
    #         visited[i][j] = 1
    #         self.solve(i-1, j, m, n, ans, move+"U", visited)
    #         visited[i][j] = 0

    def findPath(self, m: List[List[int]], n: int):
        ans = []
        visited = [[0]*n for _ in range(n)]
        di = [1, 0, 0, -1]
        dj = [0, -1, 1, 0]
        if m[0][0] == 1:
            self.solve(0, 0, m, n, ans, "", visited, di, dj)
        return ans

ans = Solution().findPath([[1,0,0,0], [1,1,0,1], [1,1,0,0], [0,1,1,1]], 4)
print(ans)