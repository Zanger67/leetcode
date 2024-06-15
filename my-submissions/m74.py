class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1

        while left < right :
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target :
                return True
            if matrix[row][col] < target :
                left = mid + 1
            else :
                right = mid
            
        mid = (left + right) // 2
        row = mid // len(matrix[0])
        col = mid % len(matrix[0])

        return matrix[row][col] == target
