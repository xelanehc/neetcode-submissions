class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        time = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    dr, dc = r + dx, c + dy
                    if dr < 0 or dr >= ROWS or dc < 0 or dc >= COLS or grid[dr][dc] != 1:
                        continue
                    fresh -= 1
                    grid[dr][dc] = 2
                    q.append((dr, dc))
            time += 1

        return time if fresh == 0 else -1