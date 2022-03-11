from typing import List

def isPossible(boards: List[int], painters: int, mid: int) -> bool:
    totalBoards = 0
    currentPainter = 1
    for board in boards:
        if totalBoards + board <= mid:
            totalBoards += board
        else:
            currentPainter += 1
            if currentPainter > painters or board > mid:
                return False
            totalBoards = board
    return True

def allocatePainer(boards: List[int], painters: int) -> int:
    totalBoards = sum(boards)
    lo, hi = 0, totalBoards
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if isPossible(boards, painters, mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

ans = allocatePainer([10, 20, 30, 40], 2)
print(ans)