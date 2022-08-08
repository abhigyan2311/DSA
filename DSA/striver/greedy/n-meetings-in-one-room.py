from math import inf

class Solution:
    def maximumMeetings(self,n,start,end):
        times = []
        for i in range(n):
            times.append((i, start[i], end[i]))
        times.sort(key=lambda x:x[2])
        meetings = []
        lastEndTime = -inf
        for i in range(0, n):
            if lastEndTime < times[i][1]: 
                meetings.append(times[i][0]+1)
                lastEndTime = times[i][2]
        return meetings
    
ans = Solution().maximumMeetings(6, [1,3,0,5,8,5], [2,4,6,7,9,9])
print(ans)
