class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.kth = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.kth:
            heapq.heappop(self.minheap)
        return self.minheap[0]
