class Solution:
    def minCoins(self, coins, M, V):
        coins.sort()
        n = len(coins)
        i = n-1
        totalCoins = []
        while i >= 0:
            while coins[i] <= V:
                V -= coins[i]
                totalCoins.append(coins[i])
            i -= 1
        return totalCoins

ans = Solution().minCoins([9, 6, 5, 1], 3, 11)
print(ans)