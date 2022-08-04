class TrieNode:
    def __init__(self) -> None:
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        count = 0
        curr = self.root
        for i in range(len(word)):
            subWord = word[i:]
            for ch in word[i:]:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                    count += 1
                curr = curr.children[ch]
            curr = self.root
        return count+1

ans = Trie().insert("abc")
print(ans)
