class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwards = [1] * len(nums)
        backwards = [1] * len(nums)

        for i in range(1,len(nums)):
            forwards[i] = forwards[i-1] * nums[i-1] 
        for i in range((len(nums) - 2),-1,-1):
            backwards[i] = backwards[i+1] * nums[i+1]
        
        return [f * b for f,b in zip(forwards,backwards)]