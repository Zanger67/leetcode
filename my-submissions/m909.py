# I hate this question so much sigh. The way it's worded is terrible.

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        linearBoard = [0]

        for i in range(len(board)) :
            if i % 2 == 0 :
                linearBoard.extend(board[len(board) - i - 1])
            else :
                linearBoard.extend(reversed(board[len(board) - i - 1]))

        toVisit = deque([(0, 1)])
        visited = set()

        while toVisit :
            steps, indx = toVisit.popleft()
            steps += 1

            if indx + 6 >= len(board) * len(board[0]) :
                return steps

            for i in range(indx + 1, indx + 7) :
                if i in visited :
                    continue
                visited.add(i)

                if linearBoard[i] != -1 :
                    if linearBoard[i] == len(board) * len(board[0]) :
                        return steps
                    toVisit.append((steps, linearBoard[i]))
                else :
                    toVisit.append((steps, i))

        return -1