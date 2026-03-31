class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')','[':']','{':'}'}

        for c in s:
            if c in pairs:
                stack.append(c)
            elif not stack or pairs[stack.pop()] != c:
                return False
        
        return True if not stack else False