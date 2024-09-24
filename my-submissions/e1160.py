class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)

        output = 0
        for word in words :
            wordCnt = Counter(word)
            if all(wordCnt[x] <= chars[x] for x in wordCnt) :
                output += len(word)

        return output
