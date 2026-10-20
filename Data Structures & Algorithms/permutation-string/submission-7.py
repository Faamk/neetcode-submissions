class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1,len2 = len(s1), len(s2)
        diff = [0] * 26

        if len1 > len2:
            return False

        for c in s1:
            diff[self.getAscValue(c)] += 1

        for c in s2[:len1]:
            diff[self.getAscValue(c)] -= 1

        
        if all(c == 0 for c in diff):
            return True

        for i in range(len1,len2):
            current_char_asc = self.getAscValue(s2[i])
            last_char_asc = self.getAscValue(s2[i - len1])
            diff[current_char_asc] -= 1
            diff[last_char_asc] += 1

            if all(c == 0 for c in diff):
                return True

        return False


    
    def getAscValue(self,ch):
        return ord(ch) - ord('a')


        