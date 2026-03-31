class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        stack = []
        valid = {'(' : ')', '[' : ']', '{' : '}'}

        for c in s:
            if c in valid:
                stack.append(c)
            elif len(stack) == 0 or valid[stack.pop()] != c:
                return False
        print(stack)
        if stack: return False
        return True