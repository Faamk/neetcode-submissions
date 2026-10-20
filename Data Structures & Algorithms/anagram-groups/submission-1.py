class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsByKey={}
        for word in strs:
            letterQuantity={}
            for c in word:
                letterQuantity[c] = letterQuantity[c] + 1 if c in letterQuantity else 1
            wordCountKey = ""
            for key in dict(sorted(letterQuantity.items())):
                wordCountKey = wordCountKey + f'{key}{letterQuantity[key]}'
            if wordCountKey in anagramsByKey:
                anagramsByKey[wordCountKey].append(word)
            else:
                anagramsByKey[wordCountKey] = [word]
        return anagramsByKey.values()


        