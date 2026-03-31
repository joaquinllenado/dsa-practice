class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash1 = {}
        hash2 = {}

        for i in range(len(s)):
            hash1[s[i]] = 1 + s.count(s[i])
            hash2[t[i]] = 1 + t.count(t[i])
        
        if hash1 == hash2:
            return True
        return False
            