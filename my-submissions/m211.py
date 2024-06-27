class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word :
            if c not in curr :
                curr[c] = {}
            curr = curr[c]
        
        curr[False] = True   # Mark end of a word

    def search(self, word: str) -> bool:
        curr = self.trie

        for i, c in enumerate(word) :
            if c == '.' :
                return any(self.searchFrom(word[i + 1:], curr[x]) for x in curr if x)

            if c not in curr :
                return False
            curr = curr[c]
        
        return False in curr

    def searchFrom(self, word, curr: dict) -> bool :
        for i, c in enumerate(word) :
            if c == '.' :
                return any(self.searchFrom(word[i + 1:], curr[x]) for x in curr if x)
            
            if c not in curr :
                return False
            curr = curr[c]

        return False in curr


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)