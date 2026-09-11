class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, cur):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return cur
            grid[r][c] = 0
            cur += 1
            cur = dfs(r + 1, c, cur)
            cur = dfs(r - 1, c, cur)
            cur = dfs(r, c + 1, cur)
            cur = dfs(r, c - 1, cur)
            return cur

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    c = dfs(row, col, 0)
                    ret = max(ret, c)
        
        return ret


        