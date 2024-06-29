class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        output = []

        for i, c in enumerate(s) :
            if not k :
                output.append(s[i:])
                break

            distToA = min(ord(c) - ord('a'), 26 - (ord(c) - ord('a')))
            if k >= distToA :
                k -= distToA
                output.append('a')
                continue

            if distToA > 0 and k :
                output.append(chr(ord(c) - k))
                k = 0

        return ''.join(output)