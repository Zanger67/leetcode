# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# This is the efficient version

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        row, col = 0, len(grid[0]) - 1

        while row < len(grid) and col >= 0 :
            if grid[row][col] < 0 :
                col -= 1
                counter += len(grid) - row
                continue
            row += 1
        
        return counter
