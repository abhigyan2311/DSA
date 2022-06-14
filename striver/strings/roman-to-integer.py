class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        exclusiveMap = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        num = 0
        n = len(s)
        i = 0
        while i<n:
            if i<n-1 and s[i:i+2] in exclusiveMap:
                num += exclusiveMap[s[i:i+2]]
                i+=1
            else:
                num += romanMap[s[i]]
            i+=1
        return num

ans = Solution().romanToInt("MCMXCIV")
print(ans)