''' This should in theory be faster than V1 since we don't have to overwrite previous
    calculations. 
    
    In the other version, we try each gate, and the spreading will occur until it reaches
    a point where it's no longer shorter, meaning each will be around the mid-point of it 
    and its nearest alternative gate.
    
    In this case, since we're iterate outwards from each gate at the same time, the moment
    visits a spot that's been visited, we know that that spot has been reached by a path
    either shorter or equal, so we can end there immediately.
'''

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        toVisit = deque()       # (row, col, stepsSoFar)
        visited = set()

        # Gate locations
        for i in range(len(rooms)) :
            for j in range(len(rooms[0])) :
                if not rooms[i][j] :
                    visited.add((i, j))             # Add gates so we don't overwrite
                    toVisit.append((i + 1, j, 1))
                    toVisit.append((i - 1, j, 1))
                    toVisit.append((i, j + 1, 1))
                    toVisit.append((i, j - 1, 1))

        while toVisit :
            row, col, stepsSoFar = toVisit.popleft()

            if not (0 <= row < len(rooms)) or not (0 <= col < len(rooms[0])) :
                continue
            
            if rooms[row][col] == -1 :
                continue

            # In theory, we should be going in increasing 
            # step order so we don't have to compare the 
            # values with the current value
            if (row, col) in visited :
                continue
            visited.add((row, col))

            rooms[row][col] = stepsSoFar
            stepsSoFar += 1

            toVisit.append((row + 1, col, stepsSoFar))
            toVisit.append((row - 1, col, stepsSoFar))
            toVisit.append((row, col + 1, stepsSoFar))
            toVisit.append((row, col - 1, stepsSoFar))



