import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,c in enumerate(numbers):
            remaining = target - c

            position_of_remainder = bisect.bisect_left(numbers,remaining)

            if position_of_remainder < len(numbers) and numbers[position_of_remainder] == remaining:
                return [i+1,position_of_remainder+1]


        