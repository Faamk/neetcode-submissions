class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        possible_keys = set(nums)
        frequencies = {k:0 for k in possible_keys}
        for n in nums:
            frequencies[n] += 1
        
        return sorted(frequencies, key=frequencies.get, reverse=True)[:k]