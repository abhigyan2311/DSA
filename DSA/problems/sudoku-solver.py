# https://leetcode.com/problems/sudoku-solver/
# https://youtu.be/FWAIf_EVUKE

from typing import Deque, List
from collections import defaultdict

class Solution:
    # O(9^(2^n)), O(1)
    # def isValid(self, board: List[List[str]], row: int, col: int, char: str) -> bool:
    #     for i in range(9):
    #         if board[row][i] == char:
    #             return False
    #         if board[i][col] == char:
    #             return False
    #         if board[3*(row//3) + i//3][3*(col//3) + i%3] == char:
    #             return False  
    #     return True
    
    # def solve(self, board: List[List[str]]) -> bool:
    #     for i in range(len(board)):
    #         for j in range(len(board[0])):
    #             if board[i][j] == ".":
    #                 for x in range(1,10):
    #                     if self.isValid(board, i, j, str(x)):
    #                         board[i][j] = str(x)
    #                         if self.solve(board) == True:
    #                             return True
    #                         else:
    #                             board[i][j] = '.'
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
                if self.solve(board, rows, cols, subBoxes, visit, vals) == True:
                    return True
                
                board[row][col] = "."
                rows[row].discard(v)
                cols[col].discard(v)
                subBoxes[t].discard(v)

        visit.append((row, col))
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, subBoxes = defaultdict(set), defaultdict(set), defaultdict(set)
        visit = []
        vals = [str(n) for n in range(1,10)]

        for row in range(9):
            for col in range(9):
                if (v := board[row][col]) != ".":
                    rows[row].add(v)
                    cols[col].add(v)
                    subBoxes[(row//3, col//3)].add(v)
                else:
                    visit.append((row, col))

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
# defaultdict(<class 'set'>, {0: {'5', '3', '7'}, 1: {'9', '5', '1', '6'}, 2: {'9', '8', '6'}, 3: {'8', '3', '6'}, 4: {'8', '3', '1', '4'}, 5: {'6', '7', '2'}, 6: {'8', '2', '6'}, 7: {'9', '5', '1', '4'}, 8: {'9', '8', '7'}})
# defaultdict(<class 'set'>, {0: {'8', '4', '5', '7', '6'}, 1: {'9', '3', '6'}, 4: {'1', '8', '2', '9', '7', '6'}, 3: {'8', '1', '4'}, 5: {'5', '3', '9'}, 2: {'8'}, 7: {'8', '7', '6'}, 8: {'1', '9', '5', '3', '6'}, 6: {'2'}})
# defaultdict(<class 'set'>, {(0, 0): {'8', '9', '5', '3', '6'}, (0, 1): {'9', '5', '1', '7'}, (0, 2): {'6'}, (1, 0): {'8', '7', '4'}, (1, 1): {'8', '3', '2', '6'}, (1, 2): {'3', '6', '1'}, (2, 0): {'6'}, (2, 2): {'8', '9', '2', '5', '7'}, (2, 1): {'9', '8', '1', '4'}})
# deque([(0, 2), (0, 3), (0, 5), (0, 6), (0, 7), (0, 8), (1, 1), (1, 2), (1, 6), (1, 7), (1, 8), (2, 0), (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), (3, 1), (3, 2), (3, 3), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 4), (4, 6), (4, 7), (5, 1), (5, 2), (5, 3), (5, 5), (5, 6), (5, 7), (6, 0), (6, 2), (6, 3), (6, 4), (6, 5), (6, 8), (7, 0), (7, 1), (7, 2), (7, 6), (7, 7), (8, 0), (8, 1), (8, 2), (8, 3), (8, 5), (8, 6)])
        