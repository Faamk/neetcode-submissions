class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            counts = {}
            for c in string:
                counts[c] = 1 if not counts.get(c) else counts[c] + 1

            ordered_counts = dict(sorted(counts.items()))
            anagram_tag = ""
            for k,v in ordered_counts.items():
                anagram_tag += f"{k}{v}"

            anagrams.setdefault(anagram_tag,[]).append(string)

        return list(anagrams.values())