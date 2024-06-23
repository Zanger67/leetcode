class Solution:
    def partitionString(self, s: str) -> int:
        lastCase: List[int] = [-1] * 26

        counter = 1
        leftPointer = 0
        for i, c in enumerate(s) :
            if lastCase[ord(c) - ord('a')] >= leftPointer :
                leftPointer = i
                counter += 1
            lastCase[ord(c) - ord('a')] = i

        return counter