from typing import List
from queue import PriorityQueue

class Solution:
    def solve(self, A: List[int], B: List[int], C: int):
        # O(N^2), O(N^2)
        # minHeap = []
        # for a in A:
        #     for b in B:
        #         heappush(minHeap, a+b)
        #         if len(minHeap) > C:
        #             heappop(minHeap)
        
        # ans = []
        # while minHeap:
        #     ans.append(heappop(minHeap))
        # return ans[::-1]
 
        # O(CLogN), O(2N)
        n = len(A)
        A.sort(reverse=True)
        B.sort(reverse=True)
        pq = PriorityQueue()
        vis = set()
        ans = []

        pq.put((-(A[0] + B[0]), (0,0)))
        vis.add((0,0))

        for _ in range(C):
            top = pq.get()
            ans.append(-top[0])

            p1 = (top[1][0] + 1, top[1][1])
            p2 = (top[1][0], top[1][1] + 1)

            if p1[0] < n and p1 not in vis:
                vis.add(p1)
                summ = A[p1[0]] + B[p1[1]]
                pq.put((-summ, p1))
            
            if p2[1] < n and p2 not in vis:
                vis.add(p2)
                summ = A[p2[0]] + B[p2[1]]
                pq.put((-summ, p2))
        
        return ans



ans = Solution().solve([1, 4, 2, 3], [2, 5, 1, 6], 4)
print(ans)
