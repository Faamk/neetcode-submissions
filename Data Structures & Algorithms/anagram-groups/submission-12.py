class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.solution_1(strs)

    def solution_1(self, strs: List[str]) -> List[List[str]]:
        counters = defaultdict(list)
        for s in strs:
            counters[tuple(sorted(s))].append(s)
        return list(counters.values())

    def solution_2(self, strs: List[str]) -> List[List[str]]:
        counters = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - 97] += 1
            counters[tuple(count)].append(s)
        return list(counters.values())
