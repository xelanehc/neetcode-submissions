class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]

        res = []

        def dfs(r):
            if r == n:
                res.append(["".join(s) for s in board])
                return
            
            for c in range(n):
                if isSafe(r, c):
                    board[r][c] = "Q"
                    dfs(r + 1)
                    board[r][c] = "."
        def isSafe(r, c):
            for i in range(0, r):
                if board[i][c] == "Q":
                    return False
                
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