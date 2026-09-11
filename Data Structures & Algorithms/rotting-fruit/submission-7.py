class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruits = 0
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fruits += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    fruits += 1

        visited = set()

        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                    or grid[r][c] == 0 or (r, c) in visited):
                    continue
                visited.add((r, c))
                grid[r][c] = 2
                fruits -= 1
                q.append((r + 1, c))
                q.append((r - 1, c))
                q.append((r, c + 1))
                q.append((r, c - 1))
            if fruits == 0:
                break
            time += 1
        
        return time if fruits == 0 else -1
