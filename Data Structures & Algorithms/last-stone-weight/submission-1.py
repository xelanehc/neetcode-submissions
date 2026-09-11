class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if y > x:
                heapq.heappush(maxHeap, x - y)
        maxHeap.append(0)
        return abs(maxHeap[0])
            
