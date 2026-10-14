class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)
        
        while len(maxHeap) > 1:
            s1 = -heapq.heappop(maxHeap)
            s2 = -heapq.heappop(maxHeap)
            diff = abs(s1 - s2)
            if diff == 0:
                continue
            heapq.heappush(maxHeap, -diff)

        return -maxHeap[0] if maxHeap else 0