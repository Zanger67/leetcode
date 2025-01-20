class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, row_len = [0] * len(mat), len(mat[0])
        cols, col_len = [0] * len(mat[0]), len(mat)

        row_col_dict = {
            val: (i, j) 
            for i, row in enumerate(mat) 
            for j, val in enumerate(row)
        }

        for i, v in enumerate(arr) :
            r, c = row_col_dict[v]

            rows[r] += 1
            cols[c] += 1

            if rows[r] == row_len or cols[c] == col_len :
                return i

        return -1