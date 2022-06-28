from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows = len(matrix)
        # cols = len(matrix[0])
        # # Transpose
        # for rowInd in range(rows):
        #     for colInd in range(0, rowInd):
        #         matrix[rowInd][colInd], matrix[colInd][rowInd] = matrix[colInd][rowInd], matrix[rowInd][colInd]
        
        # # Reverse
        # for rowInd in range(rows):
        #     colStart, colEnd = 0, cols-1
        #     while colStart < colEnd:
        #         matrix[rowInd][colStart], matrix[rowInd][colEnd] = matrix[rowInd][colEnd], matrix[rowInd][colStart]
        #         colStart += 1
        #         colEnd -= 1

        # n = len(matrix)
        # depth = n//2
        # for i in range(depth):
        #     rowLen, opp = n-1-2*i, n-1-i
        #     for j in range(rowLen):
        #         t = matrix[i][i+j]
        #         matrix[i][i+j] = matrix[opp-j][i]
        #         matrix[opp-j][i] = matrix[opp][opp-j]
        #         matrix[opp][opp-j] = matrix[i+j][opp]
        #         matrix[i+j][opp] = t

        # return matrix

        n = len(matrix)
        depth = n//2
        for i in range(depth):
            opp = n-1-i
            for j in range(opp-i):
                t = matrix[i][i+j] #top left cell
                matrix[i][i+j] = matrix[opp-j][i] #bottom left cell
                matrix[opp-j][i] = matrix[opp][opp-j] # bottom right cell
                matrix[opp][opp-j] = matrix[i+j][opp] # top right cell
                matrix[i+j][opp] = t
        return matrix

ans = Solution().rotate([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
    ])
print(ans)
                