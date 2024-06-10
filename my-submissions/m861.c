// https://leetcode.com/problems/score-after-flipping-matrix/description/


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

    for (int col = 1; col < cols; col++) {
        int count = 0;
        for (int row = 0; row < rows; row++) {
            count += grid[row][col];
        }
        if (count < gridSize / 2 || (count == gridSize / 2 && gridSize % 2 != 0)) {
            flipCol(grid, col, rows);
        }
    }


    // convert to integer
    int runningSum = 0;
    for (int row = 0; row < rows; row++) {
        int currentVal = 0;
        for (int col = 0; col < cols; col++) {
            currentVal *= 2;
            currentVal += grid[row][col];
        }
        runningSum += currentVal;
    }

    return runningSum;
    
}