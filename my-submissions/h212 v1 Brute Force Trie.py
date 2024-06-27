class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.constructTrie(words)
        output = set()
        visited = set()
        def propogate(board: List[List[str]], row: int, col: int, currentTrie: dict) -> None :
            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) :
                return
            if board[row][col] not in currentTrie :
                return

            currentTrie = currentTrie[board[row][col]]

            if False in currentTrie :
                output.add(currentTrie[False])
            
            newIndices = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for r, c in newIndices :
                if (r, c) not in visited and (0 <= r < len(board)) and (0 <= c < len(board[0])):
                    visited.add((r, c))
                    propogate(board, r, c, currentTrie)
                    visited.remove((r, c))

        for row in range(len(board)) :
            for col in range(len(board[0])) :
                visited = set()
                visited.add((row, col))
                propogate(board, row, col, trie)
            
        return list(output)
    
    def constructTrie(self, words: List[str]) -> dict :
        trie = {}

        for word in words :
            curr = trie
            for c in word :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
            curr[False] = word
        
        return trie