class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return all((n % 3 ** (x + 1)) // (3 ** x) != 2 for x in range(int(n ** (1 / 3)), -1, -1))