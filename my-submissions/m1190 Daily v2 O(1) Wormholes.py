class Solution:
    def reverseParentheses(self, s: str) -> str:
        brackets = []
        bracketPairs = {}

        # Get bracket locations and pair them with their "counterparts"
        for i, c in enumerate(s) :
            if c == ')' :
                left = brackets.pop()
                bracketPairs[left] = i
                bracketPairs[i] = left
            elif c == '(' :
                brackets.append(i)

        # Wormhole travels
        incr = 1
        indx = 0
        output = []
        while indx < len(s) :
            if indx in bracketPairs :
                indx = bracketPairs[indx]
                incr *= -1
            else :
                output.append(s[indx])
            indx += incr

        return ''.join(output)