from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        if n == 0: return ans
        intervals.sort()
        tempInterval = intervals[0]
        for nextInterval in intervals:
            if tempInterval[1] >= nextInterval[0]:
                tempInterval[1] = max(tempInterval[1], nextInterval[1])
            else:
                ans.append(tempInterval)
                tempInterval = nextInterval
        ans.append(tempInterval)
        return ans
    
ans = Solution().merge([[1,3],[2,6], [8,10], [15,18]])
print(ans)