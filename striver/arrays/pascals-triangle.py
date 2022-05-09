from typing import List


class Solution:
    # O(N^2), O(N^2)
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        prev = []
        for i in range(numRows):
            curr = []
            for j in range(i+1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(prev[j-1] + prev[j])
            prev = curr
            ans.append(curr)
        return ans

ans = Solution().generate(5)
print(ans)