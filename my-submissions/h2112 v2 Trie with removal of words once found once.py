class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Recursive propogation to search for words stemming from a specific index
        def propogate(board: List[List[str]], row: int, col: int, currentTrie) -> None :
            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) :
                return
            if board[row][col] not in currentTrie :
                return

            currentTrie = currentTrie[board[row][col]]

            if False in currentTrie :
                self.found.add(currentTrie[False])

            newIndices = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for r, c in newIndices :
                if (r, c) not in self.visited and (0 <= r < len(board)) and (0 <= c < len(board[0])):
                    self.visited.add((r, c))
                    propogate(board, r, c, currentTrie)
                    self.visited.remove((r, c))



        # Parsing through each possible origin index
        self.trie = self.constructTrie(words)
        output  = set()

        for row in range(len(board)) :
            for col in range(len(board[0])) :
                self.visited = set()
                self.found   = set()
                self.visited.add((row, col))
                propogate(board, row, col, self.trie)

                # Compiling the words we found and removing from
                # our search trie
                for fnd in self.found :
                    self.trie = self.removeWordFromTrie(fnd, self.trie)
                output |= self.found

        return list(output)
    
    # Helper method to remove a word from our trie
    def removeWordFromTrie(self, word: str, trie: dict) -> dict : 
        curr = trie
        curr['Counter'] = curr.get('Counter', 0) - 1

        if curr['Counter'] <= 0 :
            return {}

        for c in word :
            if c not in curr :
                break

            curr[c]['Counter'] = curr[c].get('Counter', 0) - 1
            if curr[c]['Counter'] <= 0 :
                curr.pop(c)
                break
            curr = curr[c]
        
        if False in curr :
            curr.pop(False)
        
        return trie


    # Helper method to create our initial trie of words that we're searching for
    def constructTrie(self, words: List[str]) -> dict :
        trie = {}

        for word in words :
            curr = trie
            trie['Counter'] = trie.get('Counter', 0) + 1
            for c in word :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
                curr['Counter'] = curr.get('Counter', 0) + 1
            curr[False] = word
        
        return trie