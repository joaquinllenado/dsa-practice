class Solution:

    def encode(self, strs: List[str]) -> str:
        codedString = ""

        for s in strs:
            codedString += str(len(s)) + "#" + s
        
        return codedString

    def decode(self, s: str) -> List[str]:
        i = 0
        decodedString = []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decodedString.append(s[i:j])
            i = j
        
        return decodedString