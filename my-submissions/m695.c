int getAreaAndVoid(int** grid, int gridSize, int* gridColSize, int x, int y) {
    if (x < 0 || y < 0 || x >= gridSize || y >= gridColSize[0] || grid[x][y] == 0) {
        return 0;
    }

    grid[x][y] = 0;

    return 1 + getAreaAndVoid(grid, gridSize, gridColSize, x + 1, y)
             + getAreaAndVoid(grid, gridSize, gridColSize, x - 1, y)
             + getAreaAndVoid(grid, gridSize, gridColSize, x, y + 1)
             + getAreaAndVoid(grid, gridSize, gridColSize, x, y - 1);
}

int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize) {
    int max = 0;

    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[0]; j++) {
            if (grid[i][j]) {
                int islandArea = getAreaAndVoid(grid, gridSize, gridColSize, i, j);
                max = (islandArea > max) ? islandArea : max;
            }
        }
    }
    return max;

    
}