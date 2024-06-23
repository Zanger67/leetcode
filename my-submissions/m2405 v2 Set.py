class Solution:
    def partitionString(self, s: str) -> int:
        current = set()

        counter = 1
        for c in s :
            if c in current :
                counter += 1
                current = set()
            current.add(c)

        return counter