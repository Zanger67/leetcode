# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        self.visited = {}
        self.case(mat, sum([sum(x) for x in mat]), 0)
        
        return self.visited.get(('0' * len(mat) * len(mat[0])), -1)

    def case(self, mat: List[List[int]], ones: int, steps: int) -> bool:
        stringify = self.toString(mat)

        if not ones :
            self.visited[stringify] = min(self.visited.get(stringify, inf), steps)
            return True

        if stringify in self.visited :
            if self.visited.get(stringify) < steps :
                return -1
        self.visited[stringify] = steps

        steps += 1
        for i in range(len(mat)) :
            for j in range(len(mat[0])) :
                tempVal = self.flip(mat, i, j)
                tempVal = self.case(mat, ones + tempVal, steps)
                self.flip(mat, i, j)
                if tempVal:
                    return False # zeros found so any more steps than this will not improve #steps
        return False

    def flip(self, mat: List[List[int]], x: int, y: int) -> int : # ret # of new 1's
        opposite = {0: 1, 1: 0}
        newOnes, newZeros = 0, 0

        mat[x][y] = opposite[mat[x][y]]
        newOnes += mat[x][y]
        newZeros += opposite[mat[x][y]]
        if x > 0 :
            mat[x - 1][y] = opposite[mat[x - 1][y]]
            newOnes += mat[x - 1][y]
            newZeros += opposite[mat[x - 1][y]]
        if x < len(mat) - 1 :
            mat[x + 1][y] = opposite[mat[x + 1][y]]
            newOnes += mat[x + 1][y]
            newZeros += opposite[mat[x + 1][y]]
        if y > 0 :
            mat[x][y - 1] = opposite[mat[x][y - 1]]
            newOnes += mat[x][y - 1]
            newZeros += opposite[mat[x][y - 1]]
        if y < len(mat[0]) - 1 :
            mat[x][y + 1] = opposite[mat[x][y + 1]]
            newOnes += mat[x][y + 1]
            newZeros += opposite[mat[x][y + 1]]

        return newOnes - newZeros


    def toString(self, mat: List[List[int]]) -> str :
        return ''.join(''.join([str(y) for y in row]) for row in mat)