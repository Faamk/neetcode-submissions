class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        answer = [k[0] for k in count.most_common(k)]
        answer.reverse()
        return answer