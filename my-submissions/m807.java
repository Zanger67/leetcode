class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[] maxByCol = new int[grid[0].length];
        int[] maxByRow = new int[grid.length];

        for (int i = 0; i < grid.length; i++) {
            maxByRow[i] = grid[i][0];
            maxByCol[i] = grid[0][i];

            for (int j = 1; j < grid[0].length; j++) {
                maxByRow[i] = Integer.max(maxByRow[i], grid[i][j]);
                maxByCol[i] = Integer.max(maxByCol[i], grid[j][i]);
            }
        }

        int output = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                output += Integer.min(maxByRow[i], maxByCol[j]) - grid[i][j];
            }
        }
        return output;
    }
}