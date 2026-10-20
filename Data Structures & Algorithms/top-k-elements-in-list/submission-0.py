class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        digit_quantity={}
        for num in nums:
            digit_quantity[num] = digit_quantity[num] + 1  if num in digit_quantity else 1
        

        sorted_digit_by_quantity=dict(sorted(digit_quantity.items(),key= lambda digit: digit[1],reverse=True))
        return list(sorted_digit_by_quantity.keys())[:k]