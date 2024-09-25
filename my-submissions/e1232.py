class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x, y = coordinates[0]
        x2, y2 = coordinates[1]
        if (x == x2 or y == y2) and (x != x2 or y != y2) :
            if x == x2 :
                return all(a == x2 for a, b in coordinates[2:])
            else :
                return all(b == y2 for a, b in coordinates[2:])

        delta = (y2 - y) / (x2 - x)

        try :
            return not any((delta != (y2 - y) / (x2 - x)) for x2, y2 in coordinates[2:])
        except ZeroDivisionError as zde :
            return False
