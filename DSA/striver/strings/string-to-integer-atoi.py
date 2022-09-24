class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        s = s.strip()
        sign = 1
        num = 0
        if not s: return num

        i=0
        if s[0] == "-": 
            sign = -1
            i += 1
        elif s[0] == "+":
            i += 1

        while i<len(s) and s[i].isdigit():
            # Can use int(s[i]) if allowed
            currDigit = ord(s[i]) - ord('0')
            if num > MAX_INT//10 or (num == MAX_INT//10 and currDigit > 7):
                return MAX_INT if sign==1 else MIN_INT
            num = num*10 + currDigit
            i += 1

        num = num*sign
        return num

ans = Solution().myAtoi("2147483648")
print(ans)