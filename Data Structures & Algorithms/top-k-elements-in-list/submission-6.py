class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.solution_2(nums,k)
    def solution_1(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [num for num,freq in count.most_common(k)]
    def solution_2(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequencies = [[] for _ in range(len(nums) + 1)]
        for num, frequency in count.items():
            frequencies[frequency].append(num)
        answer = []
        for i in range(len(frequencies) - 1,0,-1):
            for num in frequencies[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer