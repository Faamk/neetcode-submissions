class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}/{s}" for s in strs)

    def decode(self, s:str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            number_end = s.find('/',i)
            number = int(s[i:number_end])
            first_char = number_end + 1
            last_char = first_char + number
            words.append(s[first_char:last_char])
            i = last_char
        return words