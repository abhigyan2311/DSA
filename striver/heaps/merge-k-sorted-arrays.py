import heapq

class Solution:
    # def mergeKSortedkArrays(kArrays, k:int):
    #     return list(heapq.merge(*kArrays))

    def mergeKSortedkArrays(self, kArrays, k:int):
        pq = []
        for i, arr in enumerate(kArrays):
            pq.append((arr[0], i, 0))
        heapq.heapify(pq) # O(1)

        res = []
        while pq:
            num, i, j = heapq.heappop(pq)
            res.append(num)
            if j+1 < len(kArrays[i]):
                heapq.heappush(pq, (kArrays[i][j+1], i, j+1))
        return res



ans = Solution().mergeKSortedkArrays([[1, 2, 2, 3, 6, 9, 9], [0, 1, 5, 7, 9, 10], [0, 0, 1, 2, 2, 2, 7, 8]], 3)  
print(ans)