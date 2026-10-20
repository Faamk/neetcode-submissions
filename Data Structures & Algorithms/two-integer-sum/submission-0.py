class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapMissingAndIndex={}
        for index,num in enumerate(nums):
            if num in mapMissingAndIndex:
                print('Found')
                return [mapMissingAndIndex[num],index]
            else:
                mapMissingAndIndex[target - num] = index


        