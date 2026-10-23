class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [['.'] * len(board) for _ in range(len(board[0]))]
        squares = [[] for _ in range(len(board[0]))]
        for iboard,row in enumerate(board):
            for inum, number in enumerate(row):
                columns[inum][iboard] = number
                square_numer = ((inum//3) * 3) + iboard//3
                squares[square_numer].append(number)
            if not self.validateLine(row):
                return False
        for column in columns:
            if not self.validateLine(column):
                return False
        for square in squares:
            if not self.validateLine(square):
                return False
        return True
            


    

    def validateLine(self, s:List[str]) -> bool:
        print(f"Line to validate = {s}")
        no_dots = [n for n in s if n != '.']
        seen = []
        for num in no_dots:
            if not num.isdigit():
                return False
            if num in seen:
                return False
            seen.append(num)
        return True
        
        