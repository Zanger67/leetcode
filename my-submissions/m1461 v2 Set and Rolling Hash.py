class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        found = set()
        current = int(s[:k], 2)
        found.add(current)
        for i in range(k, len(s)) :
            current = (2 * current) % (2 ** k) + (ord(s[i]) - ord('0'))
            found.add(current)

        return len(found) == 2 ** k