class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0 :
            return num
        isNeg = False
        if num < 0 :
            isNeg = True
            num = -num

        digitCount = [0] * 10
        smallestDigit = 10

        while num > 0 :
            if num % 10 < smallestDigit and num % 10 != 0 :
                smallestDigit = num % 10
            digitCount[num % 10] += 1
            num //= 10

        if isNeg :  # basically get largest val
            output = 0
            for i in range(9, -1, -1) :
                for _ in range(digitCount[i]) :
                    output = 10 * output + i 
            return -1 * output

        output = smallestDigit  # since no leading zeros
        digitCount[smallestDigit] -= 1

        for i in range(10) :
            while digitCount[i] :
                output *= 10
                output += i
                digitCount[i] -= 1
        return output