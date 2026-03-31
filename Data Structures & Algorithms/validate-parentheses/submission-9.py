class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        matches = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []

        for c in s:
            if c in matches:
                stack.append(c)
            elif len(stack) == 0 or matches[stack.pop()] != c:
                return False

        if stack: return False
        return True