class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a_position = ord('a')    
        chars = [0]*26
        for a,b in zip(s,t):
            chars[ord(a) - a_position] += 1
            chars[ord(b) - a_position] -= 1
        
        return all(c==0 for c in chars)

    