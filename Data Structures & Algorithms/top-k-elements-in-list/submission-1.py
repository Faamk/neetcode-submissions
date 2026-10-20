class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = defaultdict(int)

        for num in nums:
            number_count[num] = number_count[num] + 1

        list_nums_in_order_of_appearance = list(dict(sorted(number_count.items(), key= lambda x : -x[1])).keys())



        return list_nums_in_order_of_appearance[:k]

        