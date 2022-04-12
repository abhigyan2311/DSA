from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        for op in ops:
            if op == "+":
                summ = ans[-1] + ans[-2]
                ans.append(summ)
            elif op == "D":
                doup = ans[-1] * 2
                ans.append(doup)
            elif op == "C":
                ans.pop()
            else:
                ans.append(int(op))
        res = 0
        for num in ans:
            res += num
        return res

ans = Solution().calPoints(["5","-2","4","C","D","9","+","+"])
print(ans)
