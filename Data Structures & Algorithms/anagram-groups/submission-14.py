class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.solution_3(strs)

    def solution_1(self, strs: List[str]) -> List[List[str]]:
        counters = defaultdict(list)
        for s in strs:
            counters["".join(sorted(s))].append(s)
        return list(counters.values())

    def solution_2(self, strs: List[str]) -> List[List[str]]:
        counters = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - 97] += 1
            counters[tuple(count)].append(s)
        return list(counters.values())

    def solution_3(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        counters = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in counters:
                counters[key].append(s)
            else:
                counters[key] = [s]
        return list(counters.values())
