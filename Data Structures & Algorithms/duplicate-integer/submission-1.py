class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for i,num in enumerate(nums):
            for i2,num2 in enumerate(nums):
                if num == num2 and i2 != i:
                    return True

        return False
        