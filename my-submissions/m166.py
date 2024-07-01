class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        pastDivs = dict()
        outputs = []

        if numerator == 0 :
            return '0'

        if ((numerator < 0) ^ (denominator < 0)) :
            outputs.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)

        outputs.append(str(numerator // denominator))
        numerator = (numerator % denominator) * 10
        if numerator == 0 :
            return ''.join(outputs)

        outputs.append('.')

        # Note: denominator will never chance ==> dict can be based on numerator
        while not numerator in pastDivs.keys() :
            if numerator == 0 :
                return ''.join(outputs)

            pastDivs[numerator] = len(outputs)
            outputs.append(str(numerator // denominator))
            numerator = (numerator % denominator) * 10            


        outputs.append(')')
        return ''.join(outputs[0:pastDivs.get(numerator)]) + '(' + \
               ''.join(outputs[pastDivs.get(numerator):])