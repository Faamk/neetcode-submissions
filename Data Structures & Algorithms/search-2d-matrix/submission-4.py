class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        up = 0
        down = len(matrix) - 1 

        while up <= down:
            middle = (up + down) // 2
            first_num =  matrix[middle][0]
            last_num = matrix[middle][-1]

            if target >= first_num and target <= last_num:
                row = matrix[middle]
                left = 0
                right = len(row) - 1

                while left <=right:
                    middle = (left+right) // 2
                    number = row[middle]
                    if target == number:
                        return True
                    if target > number:
                        left = middle + 1
                    else:
                        right = middle - 1
                return False
            
            if target > first_num:
                up = middle + 1
            else:
                down= middle - 1
        return False

        