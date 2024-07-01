class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)

        output = len(words)
        for word in words :
            for c in word :
                if c not in allowed :
                    output -= 1
                    break

        return output