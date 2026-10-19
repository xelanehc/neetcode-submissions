class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dists = [float('inf')] * n
        dists[src] = 0

        for i in range(k + 1):
            temp = dists.copy()

            for s, d, p in flights:
                if dists[s] == float('inf'):
                    continue
                if dists[s] + p < temp[d]:
                    temp[d] = dists[s] + p
            dists = temp
        
        return -1 if dists[dst] == float('inf') else dists[dst]