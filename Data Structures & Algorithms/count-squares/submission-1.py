class CountSquares:

    def __init__(self):
        self.hashmap = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.hashmap[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if px == x or py == y or (abs(py - y) != abs(px - x)):
                continue
            res += self.hashmap[(x, py)] * self.hashmap[(px, y)]
        return res
