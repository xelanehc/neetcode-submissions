class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        for n in arr:
            heapq.heappush(minHeap, [abs(x - n), n])
        
        res = []
        while minHeap and len(res) < k:
            dist, num = heapq.heappop(minHeap)
            res.append(num)
        
        res.sort()
        return res