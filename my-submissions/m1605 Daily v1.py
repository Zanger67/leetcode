class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        output = [[rowSum[x]] + [0] * (len(colSum) - 1) for x in range(len(rowSum))]

        for c in range(len(colSum) - 1) :
            total = 0
            indx = 0

            while indx < len(rowSum) and total < colSum[c] :
                total += output[indx][c]
                indx += 1

            indx -= 1

            output[indx][c + 1] = total - colSum[c]
            output[indx][c] -= output[indx][c + 1]

            indx += 1

            for i in range(indx, len(rowSum)) :
                output[i][c + 1] = output[i][c]
                output[i][c] = 0

        return output