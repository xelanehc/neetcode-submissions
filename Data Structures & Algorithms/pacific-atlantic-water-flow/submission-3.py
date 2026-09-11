class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, s, last):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or (r, c) in s or heights[r][c] < last):
                return
            last = heights[r][c]
            s.add((r, c))
            dfs(r + 1, c, s, last)
            dfs(r - 1, c, s, last)
            dfs(r, c + 1, s, last)
            dfs(r, c - 1, s, last)
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res