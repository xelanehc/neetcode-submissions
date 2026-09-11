class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        node = 0
        n = len(points)
        dist = [float('inf')] * n
        visited = [False] * n
        edges = 0

        while edges < n - 1:
            visited[node] = True
            nextNode = -1
            for i in range(n):
                if visited[i]:
                    continue
                curDistance = (abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDistance)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            res += dist[nextNode]
            edges += 1
            node = nextNode
        return res