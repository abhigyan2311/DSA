from math import inf
from typing import List

class Job:
    def __init__(self, id, deadline=0, profit=0) -> None:
        self.id = id
        self.profit = profit
        self.deadline = deadline

class Solution:
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs: List[(int)], n: int):
        Jobs.sort(key=lambda x:x.profit, reverse=True)
        
        maxDeadline = -inf
        for job in Jobs:
            maxDeadline = max(maxDeadline, job.deadline)
        
        times = [-1] * maxDeadline
        
        profit, counter = 0, 0
        for job in Jobs:
            idx = job.deadline - 1
            while idx >= 0 and times[idx] != -1:
                idx -= 1
            if idx < 0: continue
            times[idx] = job.id
            profit += job.profit
            counter += 1
        return counter, profit

ans = Solution().JobScheduling([
    Job(1,2,100),
    Job(2,1,19),
    Job(3,2,27), 
    Job(4,1,25),
    Job(5,1,15)
    ], 4)
print(ans)