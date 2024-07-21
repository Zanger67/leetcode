class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        counter = 0

        prev = -inf
        for x in sorted([x[0] for x in points]) :
            if x - prev <= w :
                continue
            counter += 1
            prev = x

        return counter