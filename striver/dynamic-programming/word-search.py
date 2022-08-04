from typing import List, Set, Tuple

class Solution:
    def checkIfExist(self, i: int, row: int, col: int, board: List[List[str]], word: str, rows: int, cols: int) -> bool:
        # Base Case
        if i == len(word): return True
        if min(row, col) < 0 or row >= rows or col >= cols or board[row][col] != word[i] or board[row][col] == "#" : return False

        board[row][col] = "#"
        left = self.checkIfExist(i+1, row, col-1, board, word, rows, cols)
        up = self.checkIfExist(i+1, row-1, col, board, word, rows, cols)
        right = self.checkIfExist(i+1, row, col+1, board, word, rows, cols)
        down = self.checkIfExist(i+1, row+1, col, board, word, rows, cols)
        board[row][col] = word[i]
        return left or up or right or down

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if self.checkIfExist(0, row, col, board, word, rows, cols): return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
ans = Solution().exist(board, word)
print(ans)        