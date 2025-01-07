class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [x for x in words if any(x in y and x != y for y in words)]
