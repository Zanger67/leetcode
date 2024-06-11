# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []

        for token in tokens :
            if token.isnumeric() or len(token) > 1:
                vals.append(token)
            else :
                val1, val2 = int(vals.pop()), int(vals.pop())
                match token :
                    case '+' :
                        vals.append(str(val2 + val1))
                    case '-' :
                        vals.append(str(val2 - val1))
                    case '*' :
                        vals.append(str(val2 * val1))
                    case '/' :
                        if (val1 > 0) == (val2 > 0) :
                            vals.append(str(val2 // val1))
                        else :
                            vals.append(str(-1 * (abs(val2) // abs(val1))))
        return int(vals.pop())