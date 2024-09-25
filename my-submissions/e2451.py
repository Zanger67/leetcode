class Solution:
    def oddString(self, words: List[str]) -> str:
        firstTup   = None
        foundTwice = False
        otherWord  = None

        for i, word in enumerate(words) :
            currTup = tuple(ord(word[i]) - ord(word[i - 1]) 
                            for i in range(1, len(word)))

            if not firstTup :
                firstTup = currTup
                continue

            if firstTup == currTup :
                if otherWord :
                    return otherWord
                foundTwice = True
                continue

            if not otherWord :
                if foundTwice :
                    return word
                otherWord = word
                continue

            return words[0]
