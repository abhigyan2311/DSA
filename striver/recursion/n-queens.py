# https://leetcode.com/problems/n-queens/
# https://youtu.be/i05Ju7AftcM

from typing import List

class Solution:
    # Brute Force - O(N^3), O(N^2)
    # def isValid(self, row: int, col: int, board: List[str], n: int) -> bool:
    #     rowCpy, colCpy = row, col

    #     #Check left upper diagonal
    #     while(row >= 0 and col >=0):
    #         if board[row][col] == 'Q':
    #             return False
    #         row -= 1
    #         col -= 1

    #     #Check left lower diagonal
    #     row, col = rowCpy, colCpy
    #     while(row < n and col >= 0):
    #         if board[row][col] == 'Q':
    #             return False
    #         row += 1
    #         col -= 1

    #     #Check left
    #     row, col = rowCpy, colCpy
    #     while col >= 0:
    #         if board[row][col] == 'Q':
    #             return False
    #         col -= 1

    #     return True

    # Brute Force - O(N^3), O(N^2)
    def isValid(self, row: int, col: int, board: List[str], n: int) -> bool:
        rowCpy, colCpy = row, col
        
        # Check upper left diagonal
        while row>=0 and col>=0:
            if board[row][col] == "Q": return False
            row -= 1
            col -= 1
        
        # Check left
        row, col = rowCpy, colCpy
        while col>=0:
            if board[row][col] == "Q": return False
            col -= 1
        
        row, col = rowCpy, colCpy
        # Check lower left diagonal
        while row<n and col>=0:
            if board[row][col] == "Q": return False
            row += 1
            col -= 1
        
        return True
    
    def recSolve(self, col: int, board: List[int], ans: List[List[int]], n: int):
        if col == n:
            ds = []
            for i in  range(n):
                ds.append("".join(board[i]))
            ans.append(ds[:])
            return
        for row in range(n):
            if self.isValid(row, col, board, n):
                board[row][col] = "Q"
                self.recSolve(col+1, board, ans, n)
                board[row][col] = "."
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []
        self.recSolve(0, board, ans, n)
        return ans

    # Optimized - O(N^2), O(N^2)
    # def recSolve(self, col: int, board: List[str], ans: List[List[str]], n: int, leftRow: List[int], upperDiag: List[int], lowerDiag: List[int]):
    #     if col == n:
    #         ds = []
    #         for i in range(n):
    #             ds.append(''.join(board[i]))
    #         ans.append(ds[:])
    #         return

    #     for row in range(n):
    #         if leftRow[row] == 0 and lowerDiag[row+col] == 0 and upperDiag[n-1 + col-row] == 0:
    #             board[row][col] = 'Q'
    #             leftRow[row] = 1
    #             lowerDiag[row+col] = 1
    #             upperDiag[n-1 + col-row] = 1
    #             self.recSolve(col+1, board, ans, n, leftRow, upperDiag, lowerDiag)
    #             board[row][col] = '.'
    #             leftRow[row] = 0
    #             lowerDiag[row+col] = 0
    #             upperDiag[n-1 + col-row] = 0

    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     ans = []
    #     board = []
    #     s = ['.'] * n
    #     for _ in range(n):
    #         board.append(s[:])
    #     leftRow, upperDiag, lowerDiag = [0]*n, [0]*(2*n-1), [0]*(2*n-1)
    #     self.recSolve(0, board, ans, n, leftRow, upperDiag, lowerDiag)
    #     return ans

ans = Solution().solveNQueens(4)
print(ans)