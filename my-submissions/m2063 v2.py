class Solution:
    def countVowels(self, word: str) -> int:
        vows = set('aeiou')
        return sum(i * (len(word) - i - 1) + len(word) for i, c in enumerate(word) if c in vows)
