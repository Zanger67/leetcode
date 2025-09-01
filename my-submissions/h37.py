class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_squares = [[set(), set(), set()] for _ in range(3)]
        board_rows = [set() for _ in range(9)]
        board_cols = [set() for _ in range(9)]

        for r in range(9) :
            for c in range(9) :
                if board[r][c] == '.' :
                    continue
                board_squares[r // 3][c // 3].add(board[r][c])
                board_rows[r].add(board[r][c])
                board_cols[c].add(board[r][c])

        self._helper(board, board_squares, board_rows, board_cols)

    def _helper(self, 
                board: List[List[str]], 
                board_squares, 
                board_rows, 
                board_cols, 
                r: int = 0, 
                c: int = 0) -> bool :
        if r >= 9 :
            return True

        c_next = c + 1
        r_next = r
        if c_next > 8 :
            c_next %= 9
            r_next += 1

        if board[r][c] != '.' :
            return self._helper(board, board_squares, board_rows, board_cols, r_next, c_next)
        for candidate in range(1, 10) :
            candidate_str = str(candidate)
            if (
                candidate_str in board_squares[r // 3][c // 3] or
                candidate_str in board_rows[r] or
                candidate_str in board_cols[c]
            ) :
                continue

            board[r][c] = candidate_str

            board_squares[r // 3][c // 3].add(candidate_str)
            board_rows[r].add(candidate_str)
            board_cols[c].add(candidate_str)


            if self._helper(board, board_squares, board_rows, board_cols, r_next, c_next) :
                return True

            board_squares[r // 3][c // 3].remove(candidate_str)
            board_rows[r].remove(candidate_str)
            board_cols[c].remove(candidate_str)


        board[r][c] = '.'
        return False
