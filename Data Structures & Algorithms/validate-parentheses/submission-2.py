class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'{' : '}', '[' : ']', '(' : ')'}

        for c in s:
            if c in valid:
                stack.append(c)
            elif len(stack) == 0 or valid[stack.pop()] != c:
                return False
        
        if not stack: return True
        return False