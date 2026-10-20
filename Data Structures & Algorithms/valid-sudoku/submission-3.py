class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [[] for _ in range(9)]
        lines = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]

        for i in range(0,9):
            for j in range(0,9):
               value = board[i][j]
               if(value != '.'):
                columns[j].extend(value)
                squares[i//3 * 3 + j // 3].append(board[i][j])

        for i in range(0,9):
            lines[i].extend([num for num in board[i] if num != '.'])
        
        
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




        