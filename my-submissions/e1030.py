# https://leetcode.com/problems/matrix-cells-in-distance-order/

# I'm sorry this is just funny to me lol

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[x, y] for x in range(0, rows) for y in range(0, cols)], key=lambda x: (abs(x[0] - rCenter) + abs(x[1] - cCenter)))