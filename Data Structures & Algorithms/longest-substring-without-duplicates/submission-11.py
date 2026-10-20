class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        if not s:
            return 0

        if len(s) == 1:
            return 1

        result = 0

        left = 0
        right = 0

        first_letter = s[left]

        letters_in_window = []

        while right < len(s):
            letter = s[right]
            if letter in letters_in_window:
                popped = None
                while popped != letter:
                    print(f"Looking for {letter}")
                    print(letters_in_window)
                    popped = letters_in_window.pop(0)
 
            letters_in_window.append(letter)
            result = max (result, len(letters_in_window))
            right += 1

        return max (result, len(letters_in_window))