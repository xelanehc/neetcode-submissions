class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.allpoints = []

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.allpoints.append(point)

    def count(self, point: List[int]) -> int:
        count = 0
        for curPoint in self.allpoints:
            if point == curPoint:
                continue
            if abs(curPoint[0] - point[0]) == abs(curPoint[1] - point[1]):
                count += self.points[(curPoint[0], point[1])] * self.points[(point[0], curPoint[1])]
        
        return count
