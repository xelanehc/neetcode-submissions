class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.stream = sorted(nums)

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream = sorted(self.stream)
        return self.stream[-self.kth]
