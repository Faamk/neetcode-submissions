class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i,n in enumerate(nums):
            if i>0 and n == nums[i-1]:
                continue
            idx_a = i + 1
            idx_b = len(nums) - 1            
            while idx_b > idx_a:
                three_sum = n + nums[idx_a] + nums[idx_b]
                if three_sum < 0:
                    idx_a += 1
                elif three_sum > 0:
                    idx_b-=1
                elif three_sum == 0:
                    result.append([n, nums[idx_a], nums[idx_b]])
                    idx_b -= 1
                    while nums[idx_b] == nums[idx_b+1] and idx_b > idx_a:
                        idx_b -= 1
        
        return result