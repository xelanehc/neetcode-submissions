class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, points[0][0], points[0][1])]
        res = 0
        visit = set()

        while minHeap:
            w, x, y = heapq.heappop(minHeap)
            if (x, y) in visit:
                continue
            visit.add((x, y))

            res += w
            for px, py in points:
                if (px, py) not in visit:
                    dist = abs(px - x) + abs(py - y)
                    heapq.heappush(minHeap, (dist, px, py))
        
        return res