class MagicDictionary:

    def __init__(self):
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary :
            curr = self.trie
            for c in word :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
            
            curr[False] = True

    def search(self, searchWord: str) -> bool:
        curr = self.trie
        for i, c in enumerate(searchWord) :
            if c not in curr :
                return any(self.searchNoMistakes(searchWord[i + 1 : ], curr[x]) for x in curr if x)
            elif any(self.searchNoMistakes(searchWord[i + 1 : ], curr[x]) for x in curr if x and x != c) :
                return True
            curr = curr[c]
        return False
        

    def searchNoMistakes(self, searchWord: str, curr: dict) -> bool :
        for c in searchWord :
            if c not in curr :
                return False
            curr = curr[c]
        
        return False in curr


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)