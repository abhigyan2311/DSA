from typing import List

class TrieNode:
        def __init__(self) -> None:
            self.children = {}
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
    
    def findMax(self, num):
        curr = self.root
        maxNum = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if (1-bit) in curr.children:
                maxNum = maxNum | 1<<i
                curr = curr.children[1-bit]
            else:
                curr = curr.children[bit]
        return maxNum


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        
        maxXor = 0
        for num in nums:
            xorr = trie.findMax(num)
            maxXor = max(xorr, maxXor)
        
        return maxXor