class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + sum(layer for layer in range(4, n * 4, 4))