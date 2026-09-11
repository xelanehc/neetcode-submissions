class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSquares(r, c):
            square = set()
            for i in range(3):
                for j in range(3):
                    if board[i + r][j + c] in square and board[i + r][j + c] != ".":
                        return False
                    square.add(board[i + r][j + c])
            return True
                    

        # check rows
        for i in range(9):
            row = set()
            for j in range(9):
                print(row)
                if board[i][j] in row and board[i][j] != ".":
                    return False
                row.add(board[i][j])
        # check cols
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] in col and board[i][j] != ".":
                    return False
                col.add(board[i][j])

        # check squares
        for i in range(3):
            for j in range(3):
                if not checkSquares(i * 3, j * 3):
                    return False
        
        return True