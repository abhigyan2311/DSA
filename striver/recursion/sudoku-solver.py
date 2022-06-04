# https://leetcode.com/problems/sudoku-solver/
# https://youtu.be/FWAIf_EVUKE

from typing import Deque, List
from collections import defaultdict

class Solution:
    # O(9^(2^n)), O(1)
    # def isValid(self, board: List[List[str]], row: int, col: int, char: str) -> bool:
    #     for i in range(9):
    #           if board[row][i] == char: return False
    #           if board[i][col] == char: return False
    #           if board[3*(row//3)+i//3][3*(col//3)+i%3] == char: return False
    #     return True
    
    # def solve(self, board: List[List[str]]) -> bool:
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if board[i][j] == ".":
    #                 for x in range(1,10):
    #                     if self.isValid(board, i, j, str(x)):
    #                         board[i][j] = str(x)
    #                         if self.solve(board): return True
    #                         board[i][j] = "."
    #                 return False
    #     return True

    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     self.solve(board)
    #     print(board)

    # Approach 2 - Optimized
    def solve(self, board: List[List[str]], rows, cols, subBoxes, visit, vals) -> bool:
        if not visit:
            return True
        row, col = visit.pop()
        t = (row//3, col//3)
        for v in vals:
            if v not in rows[row] and v not in cols[col] and v not in subBoxes[t]:
                board[row][col] = v
                rows[row].add(v)
                cols[col].add(v)
                subBoxes[t].add(v)
                if self.solve(board, rows, cols, subBoxes, visit, vals): return True
                board[row][col] = "."
                rows[row].remove(v)
                cols[col].remove(v)
                subBoxes[t].remove(v)
        visit.append((row, col))
        return False


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, subBoxes = defaultdict(set), defaultdict(set), defaultdict(set)
        visit = []
        vals = [str(n) for n in range(1, 10)]

        for row in range(9):
            for col in range(9):
                if (v := board[row][col]) != ".":
                    rows[row].add(v)
                    cols[col].add(v)
                    subBoxes[(row//3, col//3)].add(v)
                else:
                    visit.add((row, col))

        self.solve(board, rows, cols, subBoxes, visit, vals)
        print(board)

Solution().solveSudoku(
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    )