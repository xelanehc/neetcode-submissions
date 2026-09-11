class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        visit = set()
        minHeap = [(0, points[0][0], points[0][1])]

        while minHeap:
            dist, x, y = heapq.heappop(minHeap)
            if (x, y) in visit:
                continue
            visit.add((x,y))
            res += dist
            for px, py in points:
                if (px, py) not in visit:
                    d = abs(px - x) + abs(py - y)
                    heapq.heappush(minHeap, (d, px, py))
        
        return res