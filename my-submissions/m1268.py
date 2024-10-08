class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}

        products.sort()

        for product in products :
            curr = trie
            for c in product :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
            
            curr[False] = True

        output = []
        word = []
        for c in searchWord :
            temp = []
            if c not in trie :
                break
            trie = trie[c]
            word.append(c)
            self.counter = 3
            self.collectWordsFromPoint(trie, word, temp)
            output.append(temp)

        while len(output) < len(searchWord) :
            output.append([])


        return output

    def collectWordsFromPoint(self, trie: dict, current: List[str], output: List[str]) -> None :
        if not self.counter :
            return
        if not trie :
            return
        
        if False in trie :
            output.append(''.join(current))
            self.counter -= 1
        
        for letter, branch in trie.items() :
            if letter :
                current.append(letter)
                self.collectWordsFromPoint(branch, current, output)
                current.pop()