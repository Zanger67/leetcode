class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        xes, oes = 0, 0
        xWin, oWin = False, False

        # checking rows and getting number of each move
        for row in board :
            if all(x == 'X' for x in row) :
                xWin = True
            elif all(x == 'O' for x in row) :
                oWin = True
            xes += row.count('X')
            oes += row.count('O')

        # checking columns
        for i in range(len(board[0])) :
            if all(board[x][i] == 'X' for x in range(len(board))) :
                xWin = True
            if all(board[x][i] == 'O' for x in range(len(board))) :
                oWin = True

        # checking diagonals
        if all(board[x][x] == 'X' for x in range(len(board))) :
            xWin = True
        if all(board[x][x] == 'O' for x in range(len(board))) :
            oWin = True
        if all(board[x][len(board) - x - 1] == 'X' for x in range(len(board))) :
            xWin = True
        if all(board[x][len(board) - x - 1] == 'O' for x in range(len(board))) :
            oWin = True

        # only one can win
        if (xWin == True and oWin == True) :
            return False

        # X goes first
        if not (1 >= (xes - oes) >= 0) :
            return False

        # O can't place after X wins
        if xes == oes and xWin :
            return False

        # X can't place after O wins
        if oWin and xes > oes :
            return False

        # Valid board
        return True