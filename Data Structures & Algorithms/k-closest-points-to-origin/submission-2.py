class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for x, y in points:
            d = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(dists, (d, x, y))
        
        res = []
        for i in range(k):
            d, x, y = heapq.heappop(dists)
            res.append([x, y])
        
        return res
