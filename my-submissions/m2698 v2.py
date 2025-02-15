class Solution:
    def pot_sums(self, sqr: str, target_val: int) -> bool :
        if not sqr :
            return target_val == 0

        return any(self.pot_sums(sqr[i + 1:], target_val - int(sqr[:i + 1]))
                   for i in range(0, len(sqr)))

    def punishmentNumber(self, n: int) -> int:
        return sum(x ** 2 for x in range(1, n + 1) if self.pot_sums(str(x ** 2), x))