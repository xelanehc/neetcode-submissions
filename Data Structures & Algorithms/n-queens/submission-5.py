class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        ROWS = COLS = n
        res = []

        def dfs(r):
            if r == ROWS:
                add = ["".join(row) for row in board]
                res.append(add)
                return

            for c in range(COLS):
                if self.isValid(r, c, board):
                    board[r][c] = "Q"
                    dfs(r + 1)
                    board[r][c] = "."

        dfs(0)
        return res

    def isValid(self, row, col, board):
        r, c = row - 1, col
        while r >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1

        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        r, c = row - 1, col + 1
        while r >= 0 and c < len(board[0]):
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        
        return True