class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.backing, self.k = nums, k
        heapq.heapify(self.backing)
        while len(self.backing) > self.k:
            heapq.heappop(self.backing)

    def add(self, val: int) -> int:
        heapq.heappush(self.backing, val)
        while len(self.backing) > self.k:
            heapq.heappop(self.backing)
        return self.backing[0]
