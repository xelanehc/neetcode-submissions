class CountSquares:

    def __init__(self):
        self.countPts = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.countPts[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if x == px or y == py or (abs(px - x) != abs(py - y)):
                continue
            res += self.countPts[(x, py)] * self.countPts[(px, y)]
        return res
