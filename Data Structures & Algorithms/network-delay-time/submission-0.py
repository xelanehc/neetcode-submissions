class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {c: [] for c in range(n + 1)}
        for u, v, t in times:
            adj[u].append((v, t))
        
        visited = set()
        res = 0
        minHeap = [(0, k)]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = w1
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return res if len(visited) == n else -1