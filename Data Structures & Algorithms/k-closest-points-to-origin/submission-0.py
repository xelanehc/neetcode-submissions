import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = math.sqrt(pow(x, 2) + pow(y, 2))
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        ret = []
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            ret.append([x, y])
        return ret