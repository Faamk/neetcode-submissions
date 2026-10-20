class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right = []
        right_to_left = []
        products_of_array_except_self = []

        for i,n in enumerate(nums):
            last_number = left_to_right[i-1] if i>0 else 1
            left_to_right.insert(i, n * last_number)
        full_product = left_to_right [-1]
        for i,n in enumerate(reversed(nums)):
            last_number = right_to_left[i-1] if i>0 else 1
            right_to_left.insert(i, n * last_number)
        
        right_to_left =  list(reversed(right_to_left))

        print(f"left to right = {left_to_right}")
        print(f"right to left = {right_to_left}")

        for i,n in enumerate (nums):
            value = 0
            if i==0:
                value = right_to_left[i+1]
            elif i + 1 == len(nums):
                value = left_to_right[-2]
            else:
                value =  right_to_left[i+1] * left_to_right[i-1]

            print(f"i = {i}, value = {value}")

            products_of_array_except_self.insert(i,value)

        return products_of_array_except_self     
        