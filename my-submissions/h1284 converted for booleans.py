# Created this cause in theory for larger matrices it would be faster to use booleans instead of integers
# But in this case it doesn't matter since we're restricted to 3x3s

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        self.visited = {}
        
        zeroOneBoolMap = {0: False, 1: True}
        newMat = [[zeroOneBoolMap[x] for x in row] for row in mat]

        self.case(newMat, sum([sum(x) for x in mat]), 0)
        
        return self.visited.get(('0' * len(mat) * len(mat[0])), -1)

    def case(self, mat: List[List[bool]], ones: int, steps: int) -> bool:
        hashingMat = self.toString(mat)

        if not ones :
            self.visited[hashingMat] = min(self.visited.get(hashingMat, inf), steps)
            return True

        if hashingMat in self.visited :
            if self.visited.get(hashingMat) < steps :
                return -1
        self.visited[hashingMat] = steps

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
        newOnes, newZeros = 0, 0

        mat[x][y] = not mat[x][y]
        newOnes += mat[x][y]
        newZeros += not mat[x][y]
        if x > 0 :
            mat[x - 1][y] = not mat[x - 1][y]
            if mat[x - 1][y] :
                newOnes += 1
            else :
                newZeros += 1
        if x < len(mat) - 1 :
            mat[x + 1][y] = not mat[x + 1][y]
            if mat[x + 1][y] :
                newOnes += 1
            else :
                newZeros += 1
        if y > 0 :
            mat[x][y - 1] = not mat[x][y - 1]
            if mat[x][y - 1] :
                newOnes += 1
            else :
                newZeros += 1
        if y < len(mat[0]) - 1 :
            mat[x][y + 1] = not mat[x][y + 1]
            if matmat[x][y + 1] :
                newOnes += 1
            else :
                newZeros += 1

        return newOnes - newZeros


    def toString(self, mat: List[List[bool]]) -> str :
        zeroOnesToBool = {False: '0', True: '1'}
        return ''.join(''.join([zeroOnesToBool[y] for y in row]) for row in mat)