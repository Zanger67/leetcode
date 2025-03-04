class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x = 1
        while x * 3 <= n :
            x *= 3

        while n :
            if n - 2 * x >= 0 :
                return False
            n %= x
            x //= 3

        return True