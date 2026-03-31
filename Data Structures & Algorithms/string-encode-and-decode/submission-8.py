class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for word in strs:
            encoded_string += str(len(word)) + '#' + word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        l = r = 0
        
        while l < len(s):
            r = l

            while s[r] != '#':
                r += 1

            length = int(s[l:r])

            l = r + 1
            r = l + length

            decoded_string.append(s[l:r])

            l = r

        return decoded_string