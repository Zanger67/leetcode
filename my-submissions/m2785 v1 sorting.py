class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels, indicies = [], []

        for i, c in enumerate(s):
            if c in 'AEIOUaeiou' :
                vowels.append(c)
                indicies.append(i)

        vowels.sort()
        for j, c in zip(indicies, vowels) :
            s[j] = c

        return ''.join(s)