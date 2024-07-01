class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')


        # is just a number currently
        operators = set(list('+-*/'))
        if not any(op in s for op in operators) :
            return int(s)
        
        # operator present
        # mult and div first from left to right
        # NOTE: no brackets are present so we can just operate left to right
        expression = []
        currentNum = []
        addMin = set(list('+-'))
        for c in s :
            if c in addMin :
                expression.append(''.join(currentNum))
                currentNum = []
                if c == '-' :
                    currentNum.append('-')
            else : # numeric or */
                currentNum.append(c)

        expression.append(''.join(currentNum))

        output = 0
        for exp in expression :
            if '*' in exp or '/' in exp :
                vals = list(reversed(re.split('[*/]', exp)))
                operators = list(reversed(re.findall('[*/]', exp)))
                while operators :
                    if operators.pop() == '*' :
                        vals.append(int(vals.pop()) * int(vals.pop()))
                    else :
                        a, b = int(vals.pop()), int(vals.pop())
                        print(a, b)
                        if (a >= 0) == (b >= 0) :
                            temp = a // b
                        else :
                            temp = -1 * (abs(a) // abs(b))
                        vals.append(temp)
                output += vals.pop()
            else :
                output += int(exp)
        return output
