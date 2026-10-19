class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        visited.add(grid[0][0])
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == ROWS - 1 and c == COLS - 1:
                return t

            for dx, dy in directions:
                dr = r + dy
                dc = c + dx
                if (dr < 0 or dr >= ROWS or dc < 0 or dc >= COLS or (dr, dc) in visited):
                    continue
                visited.add((dr, dc))
                heapq.heappush(minHeap, [max(t, grid[dr][dc]), dr, dc])
        return -1