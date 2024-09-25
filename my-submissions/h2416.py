class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}

        for i, word in enumerate(words):
            curr = trie
            for c in word :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
                curr[False] = curr.get(False, 0) + 1
        output = []

        for word in words :
            curr = trie
            output.append(0)
            for i, c in enumerate(word, 1) :
                curr = curr[c]

                if False in curr :
                    output[-1] += curr[False]

        return output
