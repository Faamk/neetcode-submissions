class Solution:
    acc = 0
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return self.acc
            else:
                return -1
        middle = math.floor(len(nums)/2)

        if nums[middle] > target:
            nums = nums[:middle]
            print(f"cut to {nums}")
        else:
            nums = nums[middle:]
            self.acc += middle
            print(f"sup to {nums} and {self.acc}")

        return self.search(nums,target)
        