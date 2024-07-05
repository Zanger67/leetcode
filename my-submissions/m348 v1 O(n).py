class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        # O(2n)
        # Horizontal and vertical wins
        if not any(self.board[x][col] != player for x in range(self.n)) \
           or not any(self.board[row][x] != player for x in range(self.n)) :
           return player

        # O(n)
        # Diagonal win: top left --> bottom right \\\\
        if row == col and not any(self.board[x][x] != player for x in range(self.n)) :
            return player

        # O(n)
        # Diagonal win: bottom left --> top right ////
        if row == self.n - col - 1 and not any(self.board[x][self.n - x - 1] != player for x in range(self.n)) :
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)