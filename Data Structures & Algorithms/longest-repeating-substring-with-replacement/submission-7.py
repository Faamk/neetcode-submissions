class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        counts ={}
        l = 0
        result = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r],0)

            if r - l + 1 > max(counts.values()) + k:
                counts[s[l]] -= 1
                l += 1
            
            result = max(r - l + 1, result)


        return result