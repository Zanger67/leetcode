class DetectSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] = self.points.get((point[0], point[1]), 0) + 1

    def count(self, point: List[int]) -> int:
        output = 0

        # Normal points
        for x, y in self.points :
            if x == point[0] or y == point[1] :
                continue
            
            if ((x, point[1]) not in self.points) or ((point[0], y) not in self.points) :
                continue

            if abs(y - point[1]) != abs(x - point[0]) :
                continue

            output += self.points[(x, point[1])] * self.points[(point[0], y)] * self.points[(x, y)]

        return output


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)