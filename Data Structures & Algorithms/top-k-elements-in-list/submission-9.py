class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.solution_2(nums,k)
    
    
    def solution_1(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [num for num,freq in count.most_common(k)]
    
    
    def solution_2(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequencies = [[] for _ in range(len(nums))]
        for num,freq in count.items():
            frequencies[freq-1].append(num)
        answer = []
        for i in range(len(frequencies) - 1, -1, -1):
            digits = frequencies[i]
            for n in digits:
                answer.append(n)
                if len(answer) == k:
                    return answer
        return answer