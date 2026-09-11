class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[k - 1] = 0

        for i in range(n - 1):
            for u, v, t in times:
                if dist[v - 1] > dist[u - 1] + t:
                    dist[v - 1] = dist[u - 1] + t
        
        res = max(dist)
        return res if res != float('inf') else -1