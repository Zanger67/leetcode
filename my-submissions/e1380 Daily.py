class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowMin = [inf] * len(matrix)
        colMax = [0] * len(matrix[0])

        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] > colMax[j] :
                    colMax[j] = matrix[i][j]
                if matrix[i][j] < rowMin[i] :
                    rowMin[i] = matrix[i][j]

        return [x for x in rowMin if x in colMax]