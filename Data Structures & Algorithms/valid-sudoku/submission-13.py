class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares, lines, columns = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
               value = board[i][j]
               if value != '.':
                square_number = i//3 * 3 + j // 3
                if(value in lines[i] or value in columns[j] or value in squares[square_number]):
                    return False
                lines[i].add(value)
                columns[j].add(value)
                squares[square_number].add(value)
        return True


        