class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []
        self.total = 0

    def addNum(self, num: int) -> None:
        if self.largeHeap and num > self.largeHeap[0]:
            heapq.heappush(self.largeHeap, num)
        else:
            heapq.heappush(self.smallHeap, -num)

        if len(self.smallHeap) > len(self.largeHeap) + 1:
            transfer = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, transfer)
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            transfer = -heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, transfer)

        self.total += 1
        
    def findMedian(self) -> float:
        if len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        elif len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        else:
            return (self.largeHeap[0] + -self.smallHeap[0]) / 2
        