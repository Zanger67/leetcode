class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        output = 0
        # Top left
        for i, (_, y1) in enumerate(points) :
            # top right
            min_y = -inf
            for j, (_, y2) in enumerate(points[i + 1:], i + 1) :
                if min_y < y2 <= y1 :
                    output += 1
                    min_y = y2
                    if y1 == min_y :
                        break

        return output