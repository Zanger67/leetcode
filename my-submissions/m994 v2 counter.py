# Added a counter to save on redundancy during large LARGE maps

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Any spot in toVisit will be infected
        toVisit = deque()
        orangesLeft = 0

        # Find rotten starting points
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 2 :
                    grid[i][j] = 0
                    toVisit.append((i + 1, j, 1))
                    toVisit.append((i - 1, j, 1))
                    toVisit.append((i, j + 1, 1))
                    toVisit.append((i, j - 1, 1))
                elif grid[i][j] == 1 :
                    orangesLeft += 1
        
        turnsTaken = 0
        while toVisit and orangesLeft > 0:
            row, col, turns = toVisit.popleft()

            # out of bounds
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])) :
                continue

            # nothing there or already spoiled
            if (grid[row][col] == 0) or (grid[row][col] == 2) :
                continue
        
            # if is a non-spoiled orange
            orangesLeft -= 1
            grid[row][col] = 0
            turnsTaken = max(turnsTaken, turns)

            turns += 1
            toVisit.append((row + 1, col, turns))
            toVisit.append((row - 1, col, turns))
            toVisit.append((row, col + 1, turns))
            toVisit.append((row, col - 1, turns))

        return -1 if orangesLeft else turnsTaken