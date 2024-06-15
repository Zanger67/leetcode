class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        lettersCounter  = Counter(letters)
        wordCounters    = {w: Counter(w) for w in words}
        currentWords    = []
        self.maxScore   = 0
        
        def getAlphNum(c: str) -> int :
            return ord(c) - ord('a')

        def getScore(wordsToInclude: List[str]) -> int :        # -1 if invalid
            mergedCounters = Counter()

            for i in range(0, len(wordsToInclude)) :
                mergedCounters += wordCounters[wordsToInclude[i]]

            if any(cnt > lettersCounter.get(let, 0) for let, cnt in mergedCounters.items()) :
                return -1
            
            return sum([cnt * score[getAlphNum(let)] for let, cnt in mergedCounters.items()])


        def helper() -> None :
            if not words :
                self.maxScore = max(self.maxScore, getScore(currentWords))
            
            # if still words to add
            if words :
                nextWord = words.pop()
                helper()
                currentWords.append(nextWord)
                helper()
                words.append(currentWords.pop())

        helper()

        return self.maxScore
