class Solution:
    def totalMoney(self, n: int) -> int:
        return (
            (weeks := n // 7) * 28 + 
            (7 * weeks) * (weeks - 1) // 2 + 
            (overflow := n % 7) * weeks + 
            (1 + overflow) * overflow // 2
        )