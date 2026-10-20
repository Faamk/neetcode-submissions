class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx_a = 0
        idx_b = len(numbers)-1

        while idx_b>idx_a:
            sum_of_both = numbers[idx_a] + numbers[idx_b]
            print(sum_of_both)
            if sum_of_both > target:
                idx_b -=1
            elif sum_of_both < target:
                idx_a +=1
            else:
                return [idx_a + 1, idx_b + 1]
        