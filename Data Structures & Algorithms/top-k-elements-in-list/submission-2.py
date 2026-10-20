class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = Counter(nums)


        return [num for num, _ in number_count.most_common(k)]

        