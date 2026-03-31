class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for s in strs:
            encodedString += str(len(s)) + "#" + s
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0

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