class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word :
            if c not in curr :
                curr[c] = {}
            curr = curr[c]
        
        if False in curr :
            curr[False] += 1
        else :
            curr[False] = 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.trie
        for c in word :
            if c not in curr :
                return 0
            curr = curr[c]
        
        return curr.get(False, 0)

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.trie
        for c in prefix :
            if c not in curr :
                return 0
            curr = curr[c]
        return self.countAllFromHere(curr)
    
    def countAllFromHere(self, trie: dict) -> int :
        output = trie.get(False, 0)
        
        for k in trie :
            if k :
                output += self.countAllFromHere(trie[k])
        
        return output

    def erase(self, word: str) -> None:
        curr = self.trie
        for c in word :
            if c not in curr :
                return
            curr = curr[c]
        
        curr[False] = curr.get(False, 1) - 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)