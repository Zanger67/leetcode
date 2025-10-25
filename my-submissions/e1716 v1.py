class Solution:
    def totalMoney(self, n: int) -> int:
        output = 0
        weeks = n // 7
        output += weeks * ((7 + 1) * 7 // 2)
        output += (7 * weeks) * (weeks - 1) // 2
        overflow = n % 7
        output += overflow * weeks
        output += (1 + overflow) * overflow // 2
        return output