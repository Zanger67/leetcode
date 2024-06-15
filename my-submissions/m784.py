class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = list(s)
        
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppwercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        matches = {lowercase[x]: uppwercase[x] for x in range(len(lowercase))}
        matches.update((uppwercase[x], lowercase[x]) for x in range(len(lowercase)))

        output = []
        currentOutput = []
        
        def helper() -> None :
            if len(currentOutput) == len(s) :
                output.append(''.join(currentOutput))
                return
            
            currentOutput.append(s[len(currentOutput)])
            helper()
            currentOutput.pop()

            if s[len(currentOutput)].isnumeric() :
                return

            currentOutput.append(matches[s[len(currentOutput)]])
            helper()
            currentOutput.pop()

        helper()
        return output