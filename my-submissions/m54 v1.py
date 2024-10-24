class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 'R'     # R, L, U, D
        col_min, col_max = 0, len(matrix[0]) - 1
        row_min, row_max = 0, len(matrix) - 1
        output = []

        while col_min <= col_max and row_min <= row_max :
            match direction :
                case 'R' :
                    output.extend(matrix[row_min][col_min : col_max + 1])
                    row_min += 1
                    direction = 'D'
                case 'L' :
                    output.extend(matrix[row_max][i] for i in range(col_max, col_min - 1, -1))
                    row_max -= 1
                    direction = 'U'
                case 'U' :
                    output.extend([matrix[i][col_min] for i in range(row_max, row_min - 1, -1)])
                    col_min += 1
                    direction = 'R'
                case 'D' :
                    output.extend([matrix[i][col_max] for i in range(row_min, row_max + 1)])
                    col_max -= 1
                    direction = 'L'

        return output
