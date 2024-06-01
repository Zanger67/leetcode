// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

// v1 is inefficient since I didn't see that it was sorted both vertically
// and horizontally and that it was a static mxn matrix so I wouldn't
// have to worry about bounds.

class Solution {
    public int countNegatives(int[][] grid) {
        int counter = 0;
        int row = 0;
        int col = grid[0].length - 1;

        while (row < grid.length && col >= 0) {
            if (grid[row][col] < 0) {
                col--;
                counter += grid.length - row;
                continue;
            }
            row++;
        }

        return counter;
    }
}