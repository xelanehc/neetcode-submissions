class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {c: [] for c in range(1, n + 1)}

        for u, v, w in times:
            adj[u].append((w, v))
        
        minHeap = [(0, k)]
        visit = set()
        res = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = w1
            for w2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return res if len(visit) == n else -1
