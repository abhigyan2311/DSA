from math import inf

class Solution:
    def minimizeResult(self, expression: str) -> str:
        def evaluate(exps: str):
            return eval(exps.replace("(", "*(").replace(")", ")*").strip("*"))

        plusIndex = expression.find('+')
        n = len(expression)
        ans = [float(inf), expression]
        for l in range(plusIndex):
            for r in range(plusIndex+1, n):
                exps = f'{expression[:l]}({expression[l:plusIndex]}+{expression[plusIndex+1:r+1]}){expression[r+1:n]}'
                res = evaluate(exps)
                if ans[0] > res:
                   ans[0], ans[1] = res, exps
        return ans[1]

ans = Solution().minimizeResult("247+38")
print(ans)