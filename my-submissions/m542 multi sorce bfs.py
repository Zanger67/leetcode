class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        toVisit = deque()


        for row in range(len(mat)) :
            for col in range(len(mat[0])) :
                if mat[row][col] == 0 :
                    visited.add((row, col))
                    toVisit.append((row + 1, col, 1))
                    toVisit.append((row - 1, col, 1))
                    toVisit.append((row, col + 1, 1))
                    toVisit.append((row, col - 1, 1))

        while toVisit :
            row, col, dist = toVisit.popleft()
            if not (0 <= row < len(mat)) or not (0 <= col < len(mat[0])) :
                continue
            if (row, col) in visited :
                continue
            visited.add((row, col))

            mat[row][col] = dist
            dist += 1
            toVisit.append((row + 1, col, dist))
            toVisit.append((row - 1, col, dist))
            toVisit.append((row, col + 1, dist))
            toVisit.append((row, col - 1, dist))

        return mat