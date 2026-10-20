class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = [0]*26
        for i in range (0,len(s)):
            chars[self.cton(s[i])] += 1
            chars[self.cton(t[i])] -= 1
        
        return all(c==0 for c in chars)

    @staticmethod
    def cton (s:str):
        return ord(s) - 97

    