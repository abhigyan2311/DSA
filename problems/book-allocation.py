from typing import List

def bookAllocation(books: List[int], n: int) -> int:
    totalSum = sum(books)
    lo, hi = 0, totalSum
    ans = -1
    while lo <= hi:
        mid = (lo + hi)//2
        if isPossible(books, n, mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

def isPossible(books: List[int], n: int, mid: int) -> bool:
    studentCount, totalPages = 1, 0
    for book in books:
        if (totalPages + book <= mid):
            totalPages += book
        else:
            studentCount += 1
            if studentCount > n or book > mid:
                return False
            totalPages = book
    return True

ans = bookAllocation([5, 17, 100, 11],4)
print(ans)