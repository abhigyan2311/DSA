class TrieNode:
    def __init__(self):
        self.children = {}
        self.cntEndWord = 0
        self.cntEndPrefix = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.cntEndPrefix += 1
        cur.cntEndWord += 1
    
    def countWordsEqualTo(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.cntEndWord

    def countWordsStartingWith(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.cntEndPrefix

    def erase(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return
            curr = curr.children[ch]
            curr.cntEndPrefix -= 1
        curr.cntEndWord -= 1


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("samsung")
obj.insert("samsung")
obj.insert("sam")
obj.insert("sammy")
print(obj.countWordsEqualTo("samsung"))
obj.erase("samsung")
print(obj.countWordsEqualTo("samsung"))