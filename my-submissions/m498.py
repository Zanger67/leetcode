class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        dirr = 1
        i, j = 0, 0

        while i < len(mat) and j < len(mat[0]) :
            output.append(mat[i][j])

            if (0 <= i - dirr < len(mat)) and (0 <= j + dirr < len(mat[0])) :
                i -= dirr
                j += dirr
                continue

            # Moving up to the right
            if dirr == 1 :
                if j + 1 < len(mat[0]) :
                    j += 1
                else :
                    i += 1
                dirr *= -1
                continue

            # Moving down to the left
            if i + 1 < len(mat) :
                i += 1
            else :
                j += 1
            dirr *= -1

        return output