from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        flatGrid = [i for subList in grid for i in subList]
        while k > 0:
            flatGrid.insert(0, flatGrid.pop())
            k -= 1
        res = []
        for i in range(0, len(flatGrid), n):
            temp = []
            for x in range(n):
                temp.append(flatGrid[i+x])
            res.append(temp)   
        return res

ans = Solution().shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1)