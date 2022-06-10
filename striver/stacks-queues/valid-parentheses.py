class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for ch in s:
            if ch in dict.keys():
                stack.append(ch)
            elif ch in dict.values():
                if len(stack) == 0 or dict[stack.pop] != ch:
                    return False
        return len(stack) == 0