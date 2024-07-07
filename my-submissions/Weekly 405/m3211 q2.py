class Solution:
    def validStrings(self, n: int) -> List[str]:
        output = []

        def dfs(curr: List[str], 
                output: List[str], 
                remaining: int, 
                prevIsOne: bool) -> None :
            if not remaining :
                output.append(''.join(curr))
                return
            
            curr.append('1')
            remaining -= 1
            dfs(curr, output, remaining, True)
            curr.pop()

            if prevIsOne :
                curr.append('0')
                dfs(curr, output, remaining, False)
                curr.pop()
        dfs([], output, n, True)
        return output