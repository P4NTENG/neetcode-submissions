class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + s

        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        while len(s) > 0:
            length = int(s[0])+1
            word = s[1:length]
            decoded_strs.append(word)
            s = s[length:]

        return decoded_strs
