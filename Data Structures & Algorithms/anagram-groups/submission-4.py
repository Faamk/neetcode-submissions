class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            anagram_tag = tuple(sorted(string))
            anagrams[anagram_tag].append(string)

        return list(anagrams.values())