class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        atl, pac = set(), set()

        def dfs(r, c, last, visit):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or heights[r][c] < last:
                return
            
            visit.add((r, c))
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
        
        for r in range(ROWS):
            dfs(r, 0, float('-inf'), pac)
            dfs(r, COLS - 1, float('-inf'), atl)
        
        for c in range(COLS):
            dfs(0, c, float('-inf'), pac)
            dfs(ROWS - 1, c, float('-inf'), atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res