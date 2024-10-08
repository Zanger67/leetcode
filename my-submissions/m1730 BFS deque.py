class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        toCheck = deque()
        visited = set()

        breakLoops: bool = False
        for row in range(len(grid)) : # Examples indicate that walls are present
            if breakLoops :
                break

            for col in range(len(grid[0])) :
                if grid[row][col] == '*' :
                    toCheck.append((row, col, 0))
                    
                    breakLoops = True
                    break

        while toCheck :
            row, col, dist = toCheck.popleft()
            
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])) :
                continue
            if grid[row][col] == 'X' :
                continue
            if grid[row][col] == '#' :
                return dist
            if (row, col) in visited :
                continue
            visited.add((row, col))

            dist += 1
            toCheck.append((row + 1, col, dist))
            toCheck.append((row - 1, col, dist))
            toCheck.append((row, col + 1, dist))
            toCheck.append((row, col - 1, dist))

        return -1