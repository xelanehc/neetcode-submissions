class MedianFinder:

    def __init__(self):
        self.backing = []

    def addNum(self, num: int) -> None:
        self.backing.append(num)
        self.backing.sort()

    def findMedian(self) -> float:
        if len(self.backing) % 2:
            return self.backing[len(self.backing) // 2]
        else:
            return (self.backing[len(self.backing) // 2] + self.backing[len(self.backing) // 2 - 1]) / 2
        