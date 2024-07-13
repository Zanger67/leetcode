class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        notFound = [True] * (2 ** k)
        current = int(s[:k], 2)
        notFound[current] = False
        for i in range(k, len(s)) :
            current = (2 * current) % (2 ** k) + (ord(s[i]) - ord('0'))
            notFound[current] = False

        return not any(notFound)