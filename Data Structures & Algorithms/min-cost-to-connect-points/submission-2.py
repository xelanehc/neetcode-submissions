class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        visit = set()
        minHeap = [(0, 0)]
        res = 0
        while len(visit) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            res += cost
            for nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, nei)
        return res