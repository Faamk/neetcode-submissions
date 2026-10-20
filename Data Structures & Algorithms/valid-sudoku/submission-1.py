class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [[] for _ in range(9)]
        lines = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]

        for i in range(0,9):
            for sub_i in range(0,9):
               value = board[i][sub_i]
               if(value != '.'):
                squares[i//3 * 3 + sub_i // 3].append(board[i][sub_i])

        for i in range(0,9):
            lines[i].extend([num for num in board[i] if num != '.'])
        
        for i in range(0,9):
            for j in range(0,9):
                value = board[i][j]
                if(value != '.'):
                    columns[j].extend(value)
        
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




        