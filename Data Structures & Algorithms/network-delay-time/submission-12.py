class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {c: float('inf') for c in range(1, n + 1)}
        adj = {c: [] for c in range(n + 1)}
        for u, v, t in times:
            adj[u].append((v, t))
        
        dist[k] = 0
        q = deque([(k, 0)])
        while q:
            cur, time = q.popleft()
            if dist[cur] < time:
                continue

            for nei, w in adj[cur]:
                if time + w < dist[nei]:
                    dist[nei] = time + w
                    q.append((nei, time + w))
        
        res = max(dist.values())
        return res if res != float('inf') else -1
