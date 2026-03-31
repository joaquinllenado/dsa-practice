class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'[':']', '(':')','{':'}'}
        stack = []

        for c in s:
            if c in valid: 
                stack.append(c)
            elif len(stack) == 0 or valid[stack.pop()] != c:
                return False
        if stack:
            return False
        return True