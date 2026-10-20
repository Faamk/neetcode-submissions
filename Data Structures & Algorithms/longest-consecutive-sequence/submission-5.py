class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        nums = (list(dict.fromkeys(nums)))
        max_size = 1
        idx_a, idx_b = 0 , 1

        while idx_b > idx_a and idx_b < len(nums):
            if nums[idx_b - 1] + 1  == nums[idx_b]:
                max_size = max(max_size,(idx_b - idx_a) + 1)
                idx_b += 1
            else:
                idx_a +=1
                idx_b = idx_a + 1

        return max_size
