class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        counter = 0

        # find corners
        for r in range(len(board)) :
            for c in range(len(board[0])) :
                if board[r][c] == 'X' \
                    and (c == 0 or board[r][c - 1] == '.') \
                    and (r == 0 or board[r - 1][c] == '.'):
                    counter += 1

        return counter
