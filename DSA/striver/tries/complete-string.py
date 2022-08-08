class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isEndOfWord = True
    
    def checkIfPrefixExists(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
            if cur.isEndOfWord == False: return False
        return True

def completeString(n, a):
    trie = Trie()
    for s in a:
        trie.insert(s)
    
    longest = ""
    for s in a:
        if trie.checkIfPrefixExists(s):
            if len(s) > len(longest): longest = s
            elif len(s) == len(longest) and s < longest: longest = s
    if longest == "": return None
    return longest

ans = completeString(4, ["ab", "abc", "a", "bp"])
print(ans)

