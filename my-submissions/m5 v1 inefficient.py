class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longsetS = ''
        for i in range(len(s)) :
            for j in range(len(s) - 1, i - 1, -1) :
                if j - i + 1 <= longest :
                    continue
                isPal = True
                for k in range((j - i + 1) // 2) :
                    if s[i + k] != s[j - k] :
                        isPal = False
                        break
                if isPal :
                    longest = j - i + 1
                    longsetS = s[i: j+1]

        return longsetS