class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + ':' + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        while len(s) > 0:
            length = ""
            for i in range(0, len(s)):
                if s[i] == ':':
                    break
                length += s[i]
            length = int(length)
            word = s[1+i:1+i+length]
            decoded_strs.append(word)
            s = s[length+1+i:]

        return decoded_strs
