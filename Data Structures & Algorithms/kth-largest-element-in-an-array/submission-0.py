class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for i in nums:
            maxHeap.append(-i)
        heapq.heapify(maxHeap)
        for i in range(k - 1):
            heapq.heappop(maxHeap)
        return -heapq.heappop(maxHeap)