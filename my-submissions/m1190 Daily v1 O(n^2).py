class Solution:
    def reverseParentheses(self, s: str) -> str:
        openingIndices = []
        indx = 0
        output = list(s)

        for indx, c in enumerate(s) :
            if c == '(' :
                openingIndices.append(indx)
            elif c == ')' :
                lastOpen = openingIndices.pop()
                output[lastOpen + 1 : indx] = reversed(output[lastOpen + 1 : indx])

        return ''.join([x for x in output if x != '(' and x != ')'])