class Solution:
    def equalFrequency(self, word: str) -> bool:
        letters = [0] * 26

        for c in word :
            letters[ord(c) - ord('a')] += 1

        for i in range(26) :
            letters[i] -= 1
            if all((x == max(letters)) or (x == 0) for x in letters) :
                return True
            letters[i] += 1

        return False