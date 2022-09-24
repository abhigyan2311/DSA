class Solution:
    def intToRoman(self, num: int) -> str:
        romanList = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90),
                     ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
        roman = ""
        for symbol, value in romanList:
            if num // value > 0:
                count = num // value
                roman += symbol*count
                num %= value
        return roman


ans = Solution().intToRoman(4217)
print(ans)
