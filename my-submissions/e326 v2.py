class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 :
            return False
        while n != 1 :
            prev = n
            n //= 3
            if n * 3 != prev :
                return False

        return True