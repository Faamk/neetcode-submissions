class Solution:
    def stringtoCharMap (self, s:str) -> dict:
        mapLetter = {}
        for c in s:
            if c in mapLetter:
                mapLetter[c] = mapLetter[c] + 1
            else:
                mapLetter[c] = 1
        return mapLetter

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.stringtoCharMap(s) == self.stringtoCharMap(t)
        