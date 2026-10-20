class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        for i,num in enumerate(nums):
            if num in remainders:
                return [remainders[num], i]
            remain = target - num
            remainders[remain] = i