class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        ROWS, COLS = len(matrix), len(matrix[0])

        def dfs(r, c, last):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or matrix[r][c] <= last):
                return 0
            
            if (r, c) in cache:
                return cache[(r, c)]

            res = 1 + max(dfs(r + 1, c, matrix[r][c]), 
                dfs(r - 1, c, matrix[r][c]), 
                dfs(r, c + 1, matrix[r][c]), 
                dfs(r, c - 1, matrix[r][c]))
            cache[(r, c)] = res
            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
            
        return res