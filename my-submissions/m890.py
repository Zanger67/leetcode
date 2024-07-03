class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        currVal = 0
        hs = {}
        output = []
        for c in pattern :
            if c in hs :
                output.append(hs[c])
            else :
                output.append(currVal)
                hs[c] = currVal
                currVal += 1
                
        patternTuple = tuple(output)
        matches = []

        for word in words :
            if len(word) != len(pattern) :
                continue

            currVal = 0
            hs = {}
            output = []
            for c in word :
                if c in hs :
                    output.append(hs[c])
                else :
                    output.append(currVal)
                    hs[c] = currVal
                    currVal += 1
            if tuple(output) == patternTuple :
                matches.append(word)
        
        return matches