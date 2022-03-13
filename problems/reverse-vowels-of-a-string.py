class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        a = list(s)
        i, j = 0, len(a) - 1
        while i < j:
            if a[i].lower() not in vowels:
                i += 1
            elif a[j].lower() not in vowels:
                j -= 1
            else:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        return "".join(a)




ans = Solution().reverseVowels("leetcode")
print(ans)