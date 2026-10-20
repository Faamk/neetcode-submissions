class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = "".join(f"{len(s)}/{s}" for s in strs)

        return encoded

    def decode(self, s:str) -> List[str]:
        words = []
        i = 0
        start = 0
        while i < len(s):
            character =  s[i]
            if character == '/':
                number = int(s[start:i])
                first_char = i + 1
                last_char = first_char + number
                words.append(s[first_char:last_char])
                i = last_char
                start = i
            i += 1
        return words