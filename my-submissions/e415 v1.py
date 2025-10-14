class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        output = []

        carry = 0
        for x, y in zip_longest(reversed(num1), reversed(num2), fillvalue='0') :
            z = int(x) + int(y) + carry
            carry = z // 10
            output.append(str(z % 10))

        if carry :
            output.append('1')

        return ''.join(reversed(output))