class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return any(self.searchSpot(board, set([(row, col)]), row, col, word, 0) 
                                                    for row in range(len(board)) 
                                                    for col in range(len(board[0])))

    def searchSpot(self, 
                   board: List[List[str]], 
                   visited: Set[Tuple[int, int]],
                   row: int,
                   col: int,
                   word: str, 
                   indxOfWord: int) -> bool :

        output = False
        if board[row][col] == word[indxOfWord] :
            indxOfWord += 1
            if indxOfWord >= len(word) :
                return True

            nextSpots = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for r, c in nextSpots :
                if (0 <= r < len(board)) and (0 <= c < len(board[0])) and (r,c) not in visited :
                    visited.add((r, c))
                    output = self.searchSpot(board, visited, r, c, word, indxOfWord)
                    visited.remove((r, c))
                if output :
                    break
        
        return output