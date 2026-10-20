class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for i2 in range(i,len(nums)):
                if nums[i] == nums[i2] and i != i2:
                    return True

        return False

        