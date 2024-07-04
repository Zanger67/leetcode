class Solution:
    def reverse(self, x: int) -> int:
        val = abs(x)
        output = 0

        while val > 0 :
            output *= 10
            output += val % 10
            val = val // 10

        if x < 0 :
            output *= -1

        if output > 2 ** 31 - 1 or output < 2 ** 31 * -1 :
            return 0
        return output