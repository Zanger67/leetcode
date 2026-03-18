class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1])) # sort by x then y - note: all points are unique
        slope_intercept = defaultdict(set)
        for i, (x1, y1) in enumerate(points[:-1]) :
            for j, (x2, y2) in enumerate(points[i + 1:]) :
                if x1 == x2 : # points are guarenteed to be unique
                    m = None
                    y_intercept = x1
                else :

                    # Slope numerator denominator calculation fraction form
                    dy, dx = y2 - y1, x2 - x1
                    gcd_m = gcd(dy, dx)
                    my, mx = dy // gcd_m, dx // gcd_m
                    m = my, mx

                    # y intercept calculation fraction form
                    # y intercept = y1 - x1 * my / mx
                    #             = y1 - x1 * (y2 - y1) / (x2 - x1)
                    #             = y1 - (x1y2 - x1y1) / (x2 - x1)
                    #             = ((x2 - x1) y1 - (x1y2 - x1y1)) / (x2 - x1)
                    #             = ((x2 - x1) y1 - x1(y2 - y1)) / (x2 - x1)

                    numerator       = (x2 - x1) * y1 - x1 * (y2 - y1)
                    denominator     = x2 - x1
                    gcd_simplifier  = gcd(numerator, denominator)
                    numerator     //= gcd_simplifier
                    denominator   //= gcd_simplifier
                    y_intercept     = (numerator, denominator)

                slope_intercept[(y_intercept, m)].add((x1, y1))
                slope_intercept[(y_intercept, m)].add((x2, y2))

        if not slope_intercept :
            return 1
        return max(len(x) for x in slope_intercept.values())