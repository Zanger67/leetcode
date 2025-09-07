class Solution:
    def sumZero(self, n: int) -> List[int]:
        return (([0] if n % 2 else []) + [i for i in range(1, 1 + n // 2)] + [-i for i in range(1, 1 + n // 2)])