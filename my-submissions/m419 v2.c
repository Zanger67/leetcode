int countBattleships(char** board, int boardSize, int* boardColSize) {
    int counter = 0;

    for (int r = 0; r < boardSize; r++) {
        for (int c = 0; c < boardColSize[0]; c++) {
            if (board[r][c] == 'X'
                && (c == 0 || board[r][c - 1] == '.')
                && (r == 0 || board[r - 1][c] == '.'))
                counter++;
        }
    }
    return counter;
}

