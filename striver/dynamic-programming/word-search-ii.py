from typing import List, Set

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

class Solution:
    def checkIfExist(self, node: TrieNode, word: str, row: int, col: int, res: List[str], board: List[List[str]], rows: int, cols: int) -> None:
        # Base Case
        if min(row, col) < 0 or row >= rows or col >= cols or board[row][col] == "#": return 

        char = board[row][col]
        if char not in node.children: return

        board[row][col] = "#"

        node = node.children[char]
        word += char
        if node.isEndOfWord: 
            res.add(word)
            node.isEndOfWord = False
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            self.checkIfExist(node, word, row+dx, col+dy, res, board, rows, cols)
        board[row][col] = char

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res = []
        for row in range(rows):
            for col in range(cols):
                self.checkIfExist(root, "", row, col, res, board, rows, cols)
        return res

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
ans = Solution().findWords(board, words)
print(ans)