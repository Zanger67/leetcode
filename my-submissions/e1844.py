class Solution:
    def replaceDigits(self, s: str) -> str:
        output = []
        for i, c in enumerate(s) :
            if c.isalpha() :
                output.append(c)
            else :
                output.append(chr((int(c) + ord(s[i - 1]) - ord('a')) % 26 + ord('a')))

        return ''.join(output)