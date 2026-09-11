class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        def dfs(r, c, last):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or matrix[r][c] <= last:
                return 0
            return 1 + max(dfs(r + 1, c, matrix[r][c]),
            dfs(r - 1, c, matrix[r][c]),
            dfs(r, c + 1, matrix[r][c]),
            dfs(r, c - 1, matrix[r][c]))

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
        return res