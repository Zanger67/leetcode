class Solution:
    def numberToWords(self, num: int) -> str:
        expressions = ['', 
                        'Thousand', 
                        'Million', 
                        'Billion', 
                        'Trillion', 
                        'Quadrillion', 
                        'Quintillion', 
                        'Sextillion']

        output = []
        valsToAppend = deque()

        if num == 0:
            return 'Zero'

        while num > 0 :
            valsToAppend.appendleft(num % 1000)
            num //= 1000

        numGroups = len(valsToAppend)
        while numGroups > 0 :
            temp = self.threeDigits(valsToAppend.popleft())
            if temp != '' : # if nothing then we don't mention it
                output.append(temp)
                output.append(expressions[numGroups - 1])
            numGroups -= 1

        while output[-1].replace(' ', '') == '':
            output.pop()

        return ' '.join(output)
        
    def threeDigits(self, num: int) -> str:
        expressions = ['Zero', 
                        'One', 
                        'Two', 
                        'Three', 
                        'Four', 
                        'Five', 
                        'Six', 
                        'Seven', 
                        'Eight', 
                        'Nine', 
                        'Ten', 
                        'Eleven', 
                        'Twelve', 
                        'Thirteen', 
                        'Fourteen', 
                        'Fifteen', 
                        'Sixteen', 
                        'Seventeen', 
                        'Eighteen', 
                        'Nineteen']
        
        tens = ['', 
                '', 
                'Twenty', 
                'Thirty', 
                'Forty', 
                'Fifty', 
                'Sixty', 
                'Seventy', 
                'Eighty', 
                'Ninety']

        # We go left to right
        output = []
        if num >= 100 :
            output.append(expressions[num // 100])
            output.append('Hundred')
            num -= 100 * (num // 100)
        if num >= 20 :
            output.append(tens[num // 10])
            num -= 10 * (num // 10)
        if num < 20 and num != 0 :
            output.append(expressions[num])

        return ' '.join(output)