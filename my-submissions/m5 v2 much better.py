class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longsetS = ''
        for i in range(len(s)) :
            currOffset = 1
            while 0 <= i - currOffset and \
                  i + currOffset < len(s) and \
                  s[i - currOffset] == s[i + currOffset] :
                currOffset += 1
            currOffset -= 1

            if longest < currOffset * 2 + 1 :
                longest = currOffset * 2 + 1
                longsetS = s[i - currOffset : i + currOffset + 1]

        for i in range(0, len(s) - 1) :
            currOffset = 0
            while 0 <= i - currOffset and \
                  i + currOffset + 1 < len(s) and \
                  s[i - currOffset] == s[i + currOffset + 1] :
                currOffset += 1

            if longest < currOffset * 2 :
                longest = currOffset * 2
                longsetS = s[i - currOffset + 1 : i + currOffset + 1]

        return longsetS