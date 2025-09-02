class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        output = 0
        # Top left
        for i, (x1, y1) in enumerate(points) :
            # top right
            for j, (x2, y2) in enumerate(points[i + 1:], i + 1) :
                # valid pair
                if x2 < x1 or y2 > y1 :
                    continue
                # Check for "between" points
                if all(not (x1 <= x3 <= x2 and y2 <= y3 <= y1) for x3, y3 in points[i + 1:j]) :
                    output += 1

        return output