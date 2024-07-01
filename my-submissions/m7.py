class Solution:
    ''' Thought Process
        32-bit integer stored in 2s-comp
        1000 -> -8

        1110 -> -2
        1111 -> -1
        0000 -> 0
        0001 -> 1
        0010 -> 2
        0011 -> 3
        0100 -> 4
        0101 -> 5
        0110 -> 6
        0111 -> 7

        I feel like there's a way here but I can't find it. Or I might just be
        overthinking this tbh.
    '''
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