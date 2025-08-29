class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return ceil(n / 2) * (m // 2) + (n // 2) * ceil(m / 2)