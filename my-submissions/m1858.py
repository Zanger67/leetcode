class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: len(x))

        trie = {}
        maxx = 0
        maxxWord = ['']
        for word in words :
            curr = trie
            for i, c in enumerate(word) :
                if i == len(word) - 1 :
                    if maxx < len(word) :
                        maxx = len(word)
                        maxxWord = [word]
                    elif maxx == len(word) :
                        maxxWord.append(word)
                    
                    curr[c] = {}
                    break
                if c in curr :
                    curr = curr[c]
                else :
                    break
            
        return sorted(maxxWord)[0]