class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = defaultdict(list)
        for s in strs:
            c = Counter(s)
            key = "".join(f"{k}:{v}" for k,v in sorted(c.items()))
            counters[key].append(s)
        return list(counters.values())

