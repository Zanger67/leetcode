class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        output = []

        for i in range(len(shifts) - 2, -1, -1) :
            shifts[i] += shifts[i + 1]

        for i, c in enumerate(s) :
            output.append(chr((ord(c) - ord('a') + shifts[i]) % 26 + ord('a')))

        return ''.join(output)
