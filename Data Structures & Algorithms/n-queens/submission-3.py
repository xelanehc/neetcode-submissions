class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["."] * n for i in range(n)]
        res = []

        def dfs(r):
            if r == n:
                ans = ["".join(r) for r in grid]
                res.append(ans)
                return

            for c in range(n):
                if self.placeQueen(r, c, grid):
                    grid[r][c] = "Q"
                    dfs(r + 1)
                    grid[r][c] = "."
        
        dfs(0)
        return res
    
    def placeQueen(self, row, col, grid):
        r = row - 1
        while r >= 0:
            if grid[r][col] == "Q":
                return False
            r -= 1
        
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if grid[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        
        r, c = row - 1, col + 1
        while r >= 0 and c < len(grid):
            if grid[r][c] == "Q":
                return False
            r -= 1
            c += 1
        
        return True
    
    