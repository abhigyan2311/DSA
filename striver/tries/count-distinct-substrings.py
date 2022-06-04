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
            for ch in word[i:]:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                    count += 1
                curr = curr.children[ch]
        return count

ans = Trie().insert("sds")
print(ans)
