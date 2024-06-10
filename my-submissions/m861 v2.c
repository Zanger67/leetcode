// https://leetcode.com/problems/score-after-flipping-matrix/description/

// Optimized to not have the final loop for calculating the sum


void flipCol(int** grid, int targetCol, int numRows) {
    for (int i = 0; i < numRows; i++) {
        grid[i][targetCol] = (grid[i][targetCol] == 1) ? 0 : 1;
    }
}

void flipRow(int** grid, int targetRow, int numCols) {
    for (int i = 0; i < numCols; i++) {
        grid[targetRow][i] = (grid[targetRow][i] == 1) ? 0 : 1;
    }
}

int matrixScore(int** grid, int gridSize, int* gridColSize) {
    int rows = gridSize;
    int cols = *gridColSize;

    for (int row = 0; row < rows; row++) {
        if (!grid[row][0]) {
            flipRow(grid, row, cols);
        }
    }
    int runningSum = gridSize;

    for (int col = 1; col < cols; col++) {
        int count = 0;
        runningSum *= 2;
        for (int row = 0; row < rows; row++) {
            count += grid[row][col];
        }

        if (count < gridSize / 2 || (count == gridSize / 2 && gridSize % 2 != 0)) {
            runningSum += rows - count;
            flipCol(grid, col, rows);
        } else {
            runningSum += count;
        }
    }

    return runningSum;
}