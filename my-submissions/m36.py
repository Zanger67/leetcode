# O(3n)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        threeXthree = [defaultdict(int) for _ in range(9)]


        for i in range(len(board)) :
            for j in range(len(board[0])) :
                rows[i][board[i][j]] += 1
                cols[j][board[i][j]] += 1
                threeXthree[self.getNinth(i, j)][board[i][j]] += 1
                
                if board[i][j] != '.' and \
                    rows[i][board[i][j]] + \
                    cols[j][board[i][j]] + \
                    threeXthree[self.getNinth(i, j)][board[i][j]] > 3 :
                    return False
        return True

    def getNinth(self, x: int, y: int) -> int :
        return (3 * (x // 3)) + y // 3