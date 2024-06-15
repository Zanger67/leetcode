class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for row in range(0, len(matrix)) :
            for col in range(row + 1, len(matrix[0])) :
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(0, len(matrix)) :
            for col in range(0, len(matrix[0]) // 2) :
                matrix[row][col], matrix[row][len(matrix[0]) - col - 1] = matrix[row][len(matrix[0]) - col - 1], matrix[row][col]
