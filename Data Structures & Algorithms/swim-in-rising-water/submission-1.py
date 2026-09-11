class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        visited.add((0, 0))
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == ROWS - 1 and c == COLS - 1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                heapq.heappush(minHeap, [max(t, grid[nr][nc]), nr, nc])
            