class Solution:
    def countVowels(self, word: str) -> int:
        vows = set('aeiou')
        output = 0
        for i, c in enumerate(word) :
            if c in vows :
                output += i * (len(word) - i - 1) + len(word)
        return output