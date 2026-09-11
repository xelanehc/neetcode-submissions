class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                
        visited = set()

        d = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                    or (r, c) in visited or grid[r][c] == -1):
                        continue
                
                visited.add((r, c))
                grid[r][c] = min(grid[r][c], d)
                q.append((r + 1, c))
                q.append((r - 1, c))
                q.append((r, c + 1))
                q.append((r, c - 1))
            d += 1
        