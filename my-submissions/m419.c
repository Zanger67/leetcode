void removeShip(char** board, int boardSize, int* boardColSize, int x, int y) {
    if (x < 0 || x >= boardSize || y < 0 || y >= boardColSize[0] || board[x][y] == '.') {
        return;
    }

    board[x][y] = '.';

    removeShip(board, boardSize, boardColSize, x + 1, y);
    removeShip(board, boardSize, boardColSize, x - 1, y);
    removeShip(board, boardSize, boardColSize, x, y + 1);
    removeShip(board, boardSize, boardColSize, x, y - 1);
}

int countBattleships(char** board, int boardSize, int* boardColSize) {
    int counter = 0;

    for (int i = 0; i < boardSize; i++) {
        for (int j = 0; j < boardColSize[0]; j++) {
            if (board[i][j] == 'X') {
                counter++;
                removeShip(board, boardSize, boardColSize, i, j);
            }
        }
    }
    return counter;
}