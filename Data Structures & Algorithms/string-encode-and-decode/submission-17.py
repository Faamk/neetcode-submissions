class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += f"{string}{len(string)}/"

        return encoded


    def decode(self, s: str) -> List[str]:
        current_word = []
        words = []
        for c in s:
            if c == '/':
                word = self.validate_word(current_word)
                if word is not None:
                    words.append(word)
                    current_word = []
                    continue
            current_word.append(c)
        print(words)
        return words

    def validate_word(self, s:List):
        number = 0
        if len(s) ==1 and s[0] == '0':
            return ""
        for i,c in enumerate(s[::-1]):
            if number == len(s) - (i):
                return "".join(s[:-(i)])
            if (number > len(s) - (i)) or not c.isdigit():
                return None
            base = pow(10,i)
            number += int(c) * base

                    


