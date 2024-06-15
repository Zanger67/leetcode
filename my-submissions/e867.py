class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for row in range(0, len(matrix)) :
            for col in range(0, len(matrix[0])) :
                output[col][row] = matrix[row][col]

        return output