class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.implementation_2(s,t)

    def implementation_1(self, s:str, t:str):
        if len(s) != len(t):
            return False
        a_position = ord('a')    
        chars = [0]*26
        for a,b in zip(s,t):
            chars[ord(a) - a_position] += 1
            chars[ord(b) - a_position] -= 1
        
        return chars == [0] * 26

    def implementation_2(self, s:str, t:str):
        return Counter(s) == Counter(t)

    def implementation_3(self, s:str, t:str):
        return sorted(s) == sorted(t)
    