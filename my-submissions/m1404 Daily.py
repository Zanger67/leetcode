class Solution:
    def numSteps(self, s: str) -> int:
        counter = 0
        carry = False
        position = len(s) - 1

        while position > 0 :
            if s[position] == '0' and not carry :
                counter += 1
                position -= 1
            elif (s[position] == '0' and carry) or \
                 (s[position] == '1' and not carry) :
                counter += 2
                carry = True
                position -= 1
            else : # carry and position == 1
                counter += 1
                position -= 1
                carry = True
        
        if carry and s[0] == '1' :
            return counter + 1
        return counter