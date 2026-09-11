class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges, res = 0, 0
        n = len(points)
        dist = [float('inf')] * n
        visited = set()
        cur = 0

        while edges < n - 1:
            visited.add(cur)
            nextNode = -1
            for i in range(n):
                if i in visited:
                    continue
                curDist = abs(points[i][0] - points[cur][0]) + abs(points[i][1] - points[cur][1])
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            res += dist[nextNode]
            cur = nextNode
            edges += 1
        return res