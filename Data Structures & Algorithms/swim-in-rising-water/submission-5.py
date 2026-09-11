class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == ROWS - 1 and c == COLS - 1:
                return t
            
            for dr, dc in directions:
                cr, cc = dr + r, dc + c
                if (cr < 0 or cr >= ROWS or cc < 0 or cc >= COLS
                    or (cr, cc) in visit):
                    continue
                heapq.heappush(minHeap, (max(t, grid[cr][cc]), cr, cc))
        
        return -1