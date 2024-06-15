class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        def helper(startRow: int, startCol: int, count: int) -> None :
            if startRow < 0 \
                or startCol < 0 \
                or startRow >= len(rooms) \
                or startCol >= len(rooms[0]) :
                return

            if rooms[startRow][startCol] <= count or rooms[startRow][startCol] == -1 :
                return

            if rooms[startRow][startCol] == 0 :
                return

            rooms[startRow][startCol] = min(count, rooms[startRow][startCol])
            count += 1
            helper(startRow + 1, startCol, count)
            helper(startRow - 1, startCol, count)
            helper(startRow, startCol + 1, count)
            helper(startRow, startCol - 1, count)


        for i in range(len(rooms)) :
            for j in range(len(rooms[0])) :
                if rooms[i][j] == 0 :
                    helper(i + 1, j, 1)
                    helper(i - 1, j, 1)
                    helper(i, j + 1, 1)
                    helper(i, j - 1, 1)