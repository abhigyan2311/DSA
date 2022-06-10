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
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = [None]*n

        nums.sort()

        offlineQueries = []
        for i in range(n):
            temp = [queries[i][0], queries[i][1], i]
            offlineQueries.append(temp)
        offlineQueries.sort(key=lambda x:x[1])
        
        trie = Trie()
        
        k = 0
        for x,m,i in offlineQueries:
            while k < len(nums) and nums[k] <= m:
                trie.insert(nums[k])
                k += 1
            if k==0: ans[i] = -1
            else: ans[i] = trie.findMax(x)
        return ans

ans = Solution().maximizeXor([5,8,0,3,2,10,9,2,4,5], [[3,8]])
print(ans)