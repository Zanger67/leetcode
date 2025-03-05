class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * n // 2 * (n - 1)