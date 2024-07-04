class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        previousCase = [-1] * 26

        left = 0
        output = 0
        prevVal = 0

        for i, c in enumerate(s) :
            prev:int = previousCase[ord(c) - ord('a')]
            newVal = 1 + prevVal

            if prev != -1 and prev >= left:
                shifts = prev - left + 1
                left = prev + 1
                newVal -= shifts

            previousCase[ord(c) - ord('a')] = i
            output += newVal
            prevVal = newVal

        return output
