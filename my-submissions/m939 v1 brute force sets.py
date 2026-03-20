class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        max_area = inf
        pts = set()
        for x, y in points :
            pts.add((x, y))

        for i, (x1, y1) in enumerate(points[:-1]) :
            for j, (x2, y2) in enumerate(points[i + 1:], i + 1) :
                if (x1, y2) in pts and (x2, y1) in pts :
                    area = abs(y2 - y1) * abs(x2 - x1)
                    if area > 0 :
                        max_area = min(max_area, area)

        return max_area if max_area != inf else 0