class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = lambda x, y, z: abs(
            0.5 * (x[0] * (y[1] - z[1]) + y[0] * (z[1] - x[1]) + z[0] * (x[1] - y[1]))
        )
        output = 0
        for i, p1 in enumerate(points[:-2]) :
            for j, p2 in enumerate(points[i + 1:-1], i + 1) :
                for k, p3 in enumerate(points[j + 1:], j + 1) :
                    output = max(output, area(p1, p2, p3))

        return output