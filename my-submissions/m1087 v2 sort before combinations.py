class Solution:
    def expand(self, s: str) -> List[str]:
        outputs = []

        currentlyInBrace = False
        for c in s :
            if not currentlyInBrace :
                if c == '{' :
                    currentlyInBrace = True
                    outputs.append([])
                else:
                    outputs.append(c)
            else :
                if c == '}' :
                    outputs[-1].sort()
                    currentlyInBrace = False
                elif c != ',' :
                    outputs[-1].append(c)

        outputStrings = []
        helperOutput = []

        def helper(currIndx: int) -> None :
            if currIndx >= len(outputs) :
                outputStrings.append(''.join(helperOutput))
                return

            if isinstance(outputs[currIndx], str) :
                helperOutput.append(outputs[currIndx])
                helper(currIndx + 1)
                helperOutput.pop()
            else :
                for c in outputs[currIndx] :
                    helperOutput.append(c)
                    helper(currIndx + 1)
                    helperOutput.pop()
        helper(0)
        return outputStrings