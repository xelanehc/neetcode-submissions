class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """adj = {c: [] for c in range(n)}
        for u, v, w in flights:
            adj[u].append((w, v))"""
        
        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(k + 1):
            temp = dist.copy()
            for u, v, w in flights:
                if dist[u] == float('inf'):
                    continue
                if temp[v] > dist[u] + w:
                    temp[v] = dist[u] + w
                

            dist = temp
        
        return dist[dst] if dist[dst] != float('inf') else -1