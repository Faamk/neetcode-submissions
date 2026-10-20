class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (left+right) // 2
            num_middle = nums[middle]
            num_right = nums[right]
            num_left = nums[left]

            if num_middle == target:
                return middle

            if num_middle >= num_left:
                if num_middle > target >= num_left:
                    right = middle -1
                else:
                    left = middle + 1
            else:
                if num_middle < target <= num_right:
                    left = middle + 1
                else:
                    right = middle -1
        return -1