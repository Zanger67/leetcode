class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        letters = Counter(s)

        pairs = sum([x // 2 for x in letters.values()])
        odds = sum([x % 2 for x in letters.values()])

        return 2 * pairs + odds >= k and odds <= k
