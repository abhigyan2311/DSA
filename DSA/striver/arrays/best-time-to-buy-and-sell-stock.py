from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimal, profit = inf, 0
        for price in prices:
            minimal = min(minimal, price)
            profit = max(profit, price - minimal)
        return profit

ans = Solution().maxProfit([7,1,5,3,6,4])
print(ans)