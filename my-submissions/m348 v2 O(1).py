class TicTacToe:

    def __init__(self, n: int):
        self.boardCols = [0] * n
        self.boardRows = [0] * n
        self.diagonals = [0] * 2
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        direction = 1 if (player == 2) else -1

        self.boardCols[row] += direction
        self.boardRows[col] += direction

        if abs(self.boardCols[row]) == self.n \
            or abs(self.boardRows[col]) == self.n :
            return player
        
        if row == col :
            self.diagonals[0] += direction
            if abs(self.diagonals[0]) == self.n :
                return player

        if row == self.n - col - 1 :
            self.diagonals[1] += direction
            if abs(self.diagonals[1]) == self.n :
                return player
        
        return 0

    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)