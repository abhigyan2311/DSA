# https://www.codingninjas.com/codestudio/problems/ninja-s-training_3621003
# https://youtu.be/AE39gJYuRog

from typing import *

# Recursion - O(K^N), O(N)
# def solve(day: int, lastTask: int, points: List[List[int]]) -> int:
# 	if day == 0:
# 		maxi = 0
# 		for task in range(3):
# 			if task == lastTask: continue
# 			maxi = max(points[day][task], maxi)
# 		return maxi
	
# 	maxi = 0
# 	for task in range(3):
# 		if task == lastTask: continue
# 		totalPoints = solve(day-1, task, points) + points[day][task]
# 		maxi = max(totalPoints, maxi)
# 	return maxi

# def ninjaTraining(n: int, points: List[List[int]]) -> int:
#     return solve(n-1, 3, points)

# Recursive + Memoization - O(n*4*3), O(n) + O(n*4)
# def solve(day: int, lastTask: int, points: List[List[int]], dp: List[List[int]]) -> int:
#     if dp[day][lastTask] != -1: return dp[day][lastTask]

#     if day == 0:
#         maxi = 0
#         for task in range(3):
#             if task == lastTask: continue
#             maxi = max(points[day][task], maxi)
#         dp[day][lastTask] = maxi
#         return maxi
	
#     maxi = 0
#     for task in range(3):
#         if task == lastTask: continue
#         totalPoints = points[day][task] + solve(day-1, task, points, dp) 
#         maxi = max(totalPoints, maxi)
	
#     dp[day][lastTask] = maxi
#     return maxi

# def ninjaTraining(n: int, points: List[List[int]]) -> int:
# 	dp = [[-1] * 4 for _ in range(n)]
# 	return solve(n-1, 3, points, dp)

# Iterative + Memoization - O(n*4*3), O(n*4)
# def ninjaTraining(n: int, points: List[List[int]]) -> int:
#     dp = [[-1] * 4 for _ in range(n)]
#     dp[0][0] = max(points[0][1], points[0][2])
#     dp[0][1] = max(points[0][0], points[0][2])
#     dp[0][2] = max(points[0][0], points[0][1])
#     dp[0][3] = max(points[0][0], points[0][1], points[0][2])

#     for day in range(1, n):
#         for lastTask in range(4):
#             dp[day][lastTask] = 0
#             maxi = 0
#             for task in range(3):
#                 if task == lastTask: continue
#                 totalPoints = points[day][task] + dp[day-1][task]
#                 maxi = max(totalPoints, maxi)
#             dp[day][lastTask] = maxi
    
#     return dp[n-1][3]

# Iteration + Space Optimzation - O(N*4*3), O(4)
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    prev = [-1] * 4
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        temp = [-1] * 4
        for lastTask in range(4):
            temp[lastTask] = 0
            maxi = 0
            for task in range(3):
                if task == lastTask: continue
                totalPoints = points[day][task] + prev[task]
                maxi = max(totalPoints, maxi)
            temp[lastTask] = maxi
        prev = temp
    
    return prev[3]

ans = ninjaTraining(3, [[1,2,5], [3 ,1 ,1] ,[3,3,3]])
print(ans)