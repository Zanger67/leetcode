class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        picked = [Counter() for _ in range(n)]
        for p, b in pick :
            picked[p][b] += 1

        counter = 0
        for i in range(n) :
            if any(c >= i + 1 for c in picked[i].values()) :
                counter += 1
            pass

        return counter