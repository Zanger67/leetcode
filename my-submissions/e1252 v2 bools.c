// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/

// Swapped to using bools but for some reason it's slower than ints hm
// Memory is also worse oddly

int oddCells(int m, int n, int** indices, int indicesSize, int* indicesColSize) {
    bool** refren = (bool**) malloc(sizeof(bool*) * m);
    for (int i = 0; i < m; i++) {
        refren[i] = (bool*) malloc(sizeof(bool) * n);
        for (int j = 0; j < n; j++) {
            refren[i][j] = false;
        }
    } 

    for (int i = 0; i < indicesSize; i++) {
        // rows
        int row = indices[i][0];
        for (int j = 0; j < n; j++) {
            refren[row][j] = !refren[row][j];
        }

        // cols
        int col = indices[i][1];
        for (int j = 0; j < m; j++) {
            refren[j][col] = !refren[j][col];
        }
    }

    int output = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (refren[i][j]) {
                output++;
            }
        }
    }
    for (int i = 0; i < m; i++) {
        free(refren[i]);
    }
    free(refren);

    return output;
}