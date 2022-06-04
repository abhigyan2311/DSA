from typing import List
import math

class Solution:
    # Approach 1: BruteForce - Generate all permutations then sort the ans and return (k-1)th index element - O(n! * n + nlogn)
    def solve(self, num: List[str], numbers: List[int], permutations: List[int]):
        if len(numbers) == 0:
            permutations.append("".join(num))
            return
        for i in range(len(numbers)):
            pickedEl = numbers[i]
            num.append(str(pickedEl))
            numbers.pop(i)
            self.solve(num, numbers, permutations)
            num.pop()
            numbers.insert(i, pickedEl)

    def getPermutation(self, n: int, k: int) -> str:
        permutations = []
        numbers = list(range(1, n+1))
        self.solve([], numbers, permutations)
        return permutations[k-1]


        [1,2,3]
        
        # Approach 2: Mathematically - O(n^2), O(n)
        # numbers = list(range(1, n+1))
        # permutation = ""
        # k -= 1
        # while n > 0:
        #     n -= 1
        #     index, k = divmod(k, math.factorial(n))
        #     pickedNum = numbers[index]
        #     permutation += str(pickedNum)
        #     numbers.remove(pickedNum)
        # return permutation

ans = Solution().getPermutation(4, 17)
print(ans)