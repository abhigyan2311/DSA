from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Brute Force - O(mn * (m+n)), O(1)
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] != 0:
        #             continue
        #         else:
        #             for x in range(m):
        #                 if matrix[x][j] != 0:
        #                     matrix[x][j] = "#"
        #             for z in range(n):
        #                 if matrix[i][z] != 0:
        #                     matrix[i][z] = "#"
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == "#":
        #             matrix[i][j] = 0
        
        # Better - O(2*mn), O(m + n)
        # m = len(matrix)
        # n = len(matrix[0])
        # rows, cols = [-1]*m, [-1]*n
        # for row in range(m):
        #     for col in range(n):
        #         if matrix[row][col] == 0:
        #             rows[row] = 0
        #             cols[col] = 0
        
        # for row in range(m):
        #     for col in range(n):
        #         if rows[row] == 0 or cols[col] == 0:
        #             matrix[row][col] = 0

        # Optimal - O(2*nm), O(1)
        col0 = False
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            if matrix[i][0] == 0: col0 = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j], matrix[i][0] = 0, 0
        
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, 0, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
            if col0: matrix[i][0] = 0

        return matrix
        

ans = Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
print(ans)                