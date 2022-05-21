from typing import Dict, List, Tuple


class Solution:
    def fractionalknapsack(self, W: int, Items: List[Tuple[int, int]], n: int):
        Items.sort(key=lambda x:x[0]/x[1], reverse=True)
        currentWeight = 0
        totalVal = 0
        for item in Items:
            if currentWeight < W:
                if item[1]+currentWeight < W:
                    currentWeight += item[1]
                    totalVal += item[0]
                else:
                    remainingWeight = W - currentWeight
                    currentWeight = W
                    totalVal += item[0]/item[1] * remainingWeight
            else: break
        return totalVal


ans = Solution().fractionalknapsack(50, [(60, 10), (120, 30), (100,20)], 3)
print(ans)