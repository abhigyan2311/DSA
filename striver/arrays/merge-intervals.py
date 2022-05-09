from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        if len(intervals) == 0:
            return ans
        intervals.sort()
        tempInterval = intervals[0]
        for nextInterval in intervals:
            if nextInterval[0] <= tempInterval[1]:
                tempInterval[1] = max(nextInterval[1], tempInterval[1])
            else:
                ans.append(tempInterval)
                tempInterval = nextInterval
        ans.append(tempInterval)
        return ans
    
ans = Solution().merge([[1,4],[4,5]])
print(ans)