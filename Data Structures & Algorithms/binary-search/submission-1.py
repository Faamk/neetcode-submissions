class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left+right) // 2
            num_middle = nums[middle]

            if num_middle == target:
                return middle

            if num_middle < target:
                left = middle + 1
            else:
                right = middle - 1
            
        
        return -1
        