class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares, lines, columns = ([[] for _ in range(9)] for _ in range(3))

        for i in range(0,9):
            for j in range(0,9):
               value = board[i][j]
               if(value != '.'):
                lines[i].append(value)
                columns[j].append(value)
                squares[i//3 * 3 + j // 3].append(value)

        print (squares)
        print (lines)
        print (columns)

        for square in squares:
            if len(square) != len(set(square)):
                return False 
        for line in lines:
            if len(line) != len(set(line)):
                return False
        for column in columns:
            if len(column) != len(set(column)):
                return False 

        return True




        