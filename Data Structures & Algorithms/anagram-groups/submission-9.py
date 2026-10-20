class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = defaultdict(list)
        for s in strs:
            counters["".join(sorted(s))].append(s)
        return list(counters.values())

