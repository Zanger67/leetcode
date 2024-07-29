double probabilityOfHeads(double* prob, int probSize, int target){
    double sols[probSize + 1][target + 1];
    for (int r = 0; r < probSize + 1; r++) {
        memset(sols[r], 0, sizeof(double) * (target + 1));
    }
    sols[0][0] = 1;

    for (int r = 1; r < probSize + 1; r++) {
        sols[r][0] = sols[r - 1][0] * (1 - prob[r - 1]);
        for (int c = 1; c < target + 1; c++) {
            sols[r][c] = sols[r - 1][c] * (1 - prob[r - 1])
                            + sols[r - 1][c - 1] * prob[r - 1];
        }
    }

    return sols[probSize][target];
}