class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            print(x)
            print(y)
            if x == y:
                continue
            if y < x:
                heapq.heappush(heap, -(x - y))
        
        return -heap[0] if heap else 0