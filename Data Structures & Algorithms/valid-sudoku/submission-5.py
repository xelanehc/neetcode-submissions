class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validSquares(r, c):
            s = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
            return True
        
        # check for rows
        for r in range(9):
            s = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in s:
                    return False
                s.add(board[r][c])
        
        # check for columns
        for c in range(9):
            s = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in s:
                    return False
                s.add(board[r][c])

        # check for squares
        for r in range(3):
            for c in range(3):
                if not validSquares(r * 3, c * 3):
                    return False
        return True