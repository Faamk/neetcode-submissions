class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares, lines, columns = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]

        for line in range(9):
            for column in range(9):
               value = board[line][column]
               if value != '.':
                square_number = line//3 * 3 + column // 3
                if(value in lines[line] or value in columns[column] or value in squares[square_number]):
                    return False
                lines[line].add(value)
                columns[column].add(value)
                squares[square_number].add(value)
        return True


        