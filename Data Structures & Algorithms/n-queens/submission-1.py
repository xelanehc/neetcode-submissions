class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        def dfs(r):
            if r == n:
                add = ["".join(s) for s in board]
                res.append(add)
                return
            
            for c in range(n):
                if isSafe(r, c):
                    board[r][c] = "Q"
                    dfs(r + 1)
                    board[r][c] = "."
        
        def isSafe(r, c):
            row = r
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1
            
            row, col = r, c
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row, col = row - 1, col - 1
            
            row, col = r, c
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                row, col = row - 1, col + 1
            
            return True

        dfs(0)
        return res
