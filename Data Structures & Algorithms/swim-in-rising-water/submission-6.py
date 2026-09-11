class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minHeap = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visit = set()

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return t
            visit.add((r, c))
            for dr, dc in directions:
                cr, cc = r + dr, c + dc
                if cr < 0 or cr >= ROWS or cc < 0 or cc >= COLS:
                    continue
                if (cr, cc) not in visit:
                    heapq.heappush(minHeap, (max(t, grid[cr][cc]), cr, cc))