class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        visited = set()
        minHeap = [[0, 0]]
        while len(visited) < len(points):
            dist, cur = heapq.heappop(minHeap)
            if cur in visited:
                continue
            res += dist
            visited.add(cur)
            for w, nei in adj[cur]:
                if nei not in visited:
                    heapq.heappush(minHeap, [w, nei])
        
        return res