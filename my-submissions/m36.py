# https://leetcode.com/problems/valid-sudoku/
# O(3n)

''' Ideas
    If we iterate through each row, col, and box, we can do it in O(3n)
    We can have a map for each with the counter of how many of each value
    If the sum of any square > 3 then we return false
'''

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