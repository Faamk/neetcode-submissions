class Solution:

        
    def add_word_or_character(self,current_word, words, c):
        if c == '#':
            if current_word:
                size = 0
                i = 0
                string = current_word[i+1:]
                while size < len(current_word) and current_word[i].isdigit():
                    string = current_word[i+1:]
                    n = current_word[i]
                    size = size + (int(n) * pow(10,i))
                    i = i + 1
                    print(f'Size: {size}, string: {string} - Match: {size == len(string)}, c: {c}')
                    if size == len(string):
                        current_word.clear()
                        words.append(''.join(reversed(string)))
                        return
                current_word+=c
        else:
            current_word+=c


    def encode(self, strs: List[str]) -> str:
        compacted_str = ""
        for word in strs:
            compacted_str += word + f'{len(word)}' + '#'
        return compacted_str[::-1] + '#'

    def decode(self, s: str) -> List[str]:
        words=[]
        current_word=[]
        print(s)
        for c in s:
            self.add_word_or_character(current_word, words, c)
            
        return words[::-1]


