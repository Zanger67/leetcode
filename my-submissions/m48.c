void rotate(int** matrix, int matrixSize, int* matrixColSize) {
    for (int row = 0; row < matrixSize; row++) {
        for (int col = row + 1; col < matrixSize; col++) {
            int holder = matrix[row][col];
            matrix[row][col] = matrix[col][row];
            matrix[col][row] = holder;
        }
    }
    
    for (int row = 0; row < matrixSize; row++) {
        for (int col = 0; col < matrixSize / 2; col++) {
            int holder = matrix[row][col];
            matrix[row][col] = matrix[row][matrixSize - col - 1];
            matrix[row][matrixSize - col - 1] = holder;
        }
    }
    
}