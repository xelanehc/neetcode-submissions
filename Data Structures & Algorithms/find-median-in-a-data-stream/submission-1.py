class MedianFinder:

    def __init__(self):
        self.backing = []

    def addNum(self, num: int) -> None:
        self.backing.append(num)

    def findMedian(self) -> float:
        self.backing.sort()
        n = len(self.backing)
        if n % 2 == 1:
            return self.backing[n // 2]
        else:
            return (self.backing[n // 2] + self.backing[n // 2 - 1]) / 2
        
        