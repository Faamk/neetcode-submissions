class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares, lines, columns = ([[] for _ in range(9)] for _ in range(3))

        for i in range(0,9):
            for j in range(0,9):
               value = board[i][j]
               square_number = i//3 * 3 + j // 3
               if(value != '.'):
                if(value in lines[i] or value in columns[j] or value in squares[square_number]):
                    return False
                lines[i].append(value)
                columns[j].append(value)
                squares[square_number].append(value)
        return True


        