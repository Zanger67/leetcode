class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum([x * ceil(i / 8) for i, x in enumerate(sorted([f for f in Counter(word).values()], reverse=True), 1)])