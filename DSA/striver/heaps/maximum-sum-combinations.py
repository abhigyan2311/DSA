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

        pq.put((-(A[0] + B[0]), (0, 0)))
        vis.add((0, 0))

        for _ in range(C):
            summ, pos = pq.get()
            ans.append(-summ)

            pos1 = (pos[0] + 1, pos[1])
            pos2 = (pos[0], pos[1] + 1)

            if pos1[0] < n and pos1 not in vis:
                vis.add(pos1)
                summ = A[pos1[0]] + B[pos1[1]]
                pq.put((-summ, pos1))

            if pos2[1] < n and pos2 not in vis:
                vis.add(pos2)
                summ = A[pos2[0]] + B[pos2[1]]
                pq.put((-summ, pos2))

        return ans


ans = Solution().solve([1, 4, 2, 3], [2, 5, 1, 6], 4)
print(ans)
