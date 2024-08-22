class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(curr: List[str] = [],
                currIndx: int = 0,
                currNum: int = 0,
                output: List[str] = []) -> List[str] :

            if currIndx >= len(word) :
                output.append(''.join(curr) + ('' if currNum <= 0 else str(currNum)))
                return output

            # we have numbers in storage
            if currNum > 0 :
                # include number NOW
                curr.append(str(currNum))       # add number
                curr.append(word[currIndx])     # add current letter as separator
                dfs(curr, currIndx + 1, 0, output)
                curr.pop()                      # pop for space reuse
                curr.pop()                      # pop for space reuse

                # wait on number by just adding to existing count
                dfs(curr, currIndx + 1, currNum + 1, output)

            # we have no numbers in storage
            else :
                # set current letter as start of abbreviated section
                dfs(curr, currIndx + 1, 1, output)

                # put in as a letter
                curr.append(word[currIndx])
                dfs(curr, currIndx + 1, 0, output)
                curr.pop()                      # pop for space reuse

            return output

        return dfs()
