class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''.join(c.lower() for c in s if c.isalnum()).strip()
        return clean_str == clean_str[::-1]
        