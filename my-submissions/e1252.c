// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/


// Lot of loops but eh ill swap it around with bools


int oddCells(int m, int n, int** indices, int indicesSize, int* indicesColSize) {

    // reference matrix setup
    int** refren = (int**) malloc(sizeof(int*) * m);
    for (int i = 0; i < m; i++) {
        refren[i] = (int*) malloc(sizeof(int) * n);
        for (int j = 0; j < n; j++) {
            refren[i][j] = 0;
        }
    } 

    // calculations
    for (int i = 0; i < indicesSize; i++) {
        // rows
        int row = indices[i][0];
        for (int j = 0; j < n; j++) {
            refren[row][j]++;
        }

        // cols
        int col = indices[i][1];
        for (int j = 0; j < m; j++) {
            refren[j][col]++;
        }
    }

    // counting odds
    int output = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (refren[i][j] % 2 == 1) {
                output++;
            }
        }
    }

    // freeing
    for (int i = 0; i < m; i++) {
        free(refren[i]);
    }
    free(refren);
    
    // output
    return output;
}