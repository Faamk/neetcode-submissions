class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_data = ""
        for string in strs:
            encoded_data += f"{string}#{Counter(string).total()}"
        print(encoded_data)
        return encoded_data

    def decode(self, s: str) -> List[str]:
        list_of_words = []
        current_word_letter_count = 0
        current_word = ""
        count_word = ""

        for i, c in enumerate(s):
            print (count_word)
            if c == '#' and not count_word:
                count_word +=c
            else:
                if count_word:
                    if c.isdigit():
                        count_word += c    
                        if int(count_word[1:]) == len(current_word):
                            list_of_words.append(current_word)
                            current_word_letter_count = 0
                            current_word = ""
                            count_word = ""
                    else: 
                        current_word += count_word
                        count_word = ""
                        count_word += c
                else:
                    current_word += count_word
                    count_word = ""
                    current_word += c

        return list_of_words