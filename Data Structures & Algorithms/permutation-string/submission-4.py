class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        current_str = s1
        right = 0
        while right < len(s2):
            if not current_str:
                return True

            letter = s2[right]

            if letter in current_str:
                current_str = current_str.replace(letter, "", 1)
            else:
                right -= len(s1) - len(current_str)
                current_str = s1
            right += 1

        return not current_str

        