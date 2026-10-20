class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_map = {}
        for i, num in enumerate(nums):
            if num in result_map:
                return [result_map[num], i]
            else:
                result_map[target - num] = i