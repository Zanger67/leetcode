class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        output = 0

        cases = [[[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                 [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
                 [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                 [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                 [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                 [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                 [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                 [[8, 1, 6], [3, 5, 7], [4, 9, 2]]]

        for r in range(len(grid) - 2) :
            for c in range(len(grid[0]) - 2) :
                if [grid[r + i][c : c + 3] for i in range(3)] in cases :
                    output += 1

        return output