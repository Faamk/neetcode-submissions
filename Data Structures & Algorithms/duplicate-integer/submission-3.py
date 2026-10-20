class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(0,len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = True

        return False

        